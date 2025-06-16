import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from openai import AzureOpenAI
import os
import json
import re

# --- Azure OpenAI Setup ---
AZURE_OPENAI_ENDPOINT = "https://cmf-ai-foundry.cognitiveservices.azure.com/"
API_KEY = "8IHKWwsPG4sY44e4BgcBmS9Dyh2evwfJZkBjDbbxUeMuTvsxkcKpJQQJ99BFACYeBjFXJ3w3AAAAACOG5GOx"
DEPLOYMENT_NAME = "gpt-4.1-2"
HISTORY_FILE = "chat_history.json"

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=API_KEY,
    api_version="2025-01-01-preview"
)

# --- Chat History ---
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return [{"role": "system", "content": "You are a helpful AI assistant."}]

def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def export_chat():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            for msg in history:
                if msg["role"] == "user":
                    f.write(f"You: {msg['content']}\n")
                elif msg["role"] == "assistant":
                    f.write(f"Assistant: {msg['content']}\n\n")

# --- Markdown Formatter (very basic highlighting) ---
def insert_markdown(text_widget, content):
    lines = content.split('\n')
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            tag = "code"
            continue  # skip the ```
        tag = "code" if in_code_block else "normal"
        text_widget.insert(tk.END, line + '\n', tag)
    text_widget.insert(tk.END, '\n')

# --- Send Message ---
def send_message():
    user_input = entry.get("1.0", tk.END).strip()
    if not user_input:
        return

    entry.delete("1.0", tk.END)
    chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_window.insert(tk.END, "\n")

    history.append({"role": "user", "content": user_input})

    status_var.set("Assistant is typing...")
    root.update_idletasks()

    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=history
        )
        assistant_reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": assistant_reply})
        insert_markdown(chat_window, "Assistant: " + assistant_reply)
        chat_window.insert(tk.END, "\n")
        chat_window.see(tk.END)
        save_history()
    except Exception as e:
        chat_window.insert(tk.END, f"Error: {e}\n\n", "error")

    status_var.set("Ready")

# --- Reset Chat ---
def reset_chat():
    global history
    history = [{"role": "system", "content": "You are a helpful AI assistant."}]
    chat_window.delete("1.0", tk.END)
    status_var.set("New chat started.")
    save_history()

# --- GUI Setup ---
root = tk.Tk()
root.title("Chat with GPT-4.1 (Azure)")
root.geometry("800x700")

chat_window = ScrolledText(root, wrap=tk.WORD, height=25, width=100)
chat_window.pack(padx=10, pady=10)

entry = ScrolledText(root, height=5, width=100)
entry.pack(padx=10, pady=(0, 10))

# --- Button Frame ---
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 10))

send_button = tk.Button(button_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="New Chat", command=reset_chat)
reset_button.pack(side=tk.LEFT, padx=5)

export_button = tk.Button(button_frame, text="Export Chat", command=export_chat)
export_button.pack(side=tk.LEFT, padx=5)

# --- Status Bar ---
status_var = tk.StringVar()
status_var.set("Ready")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

# --- Text Formatting ---
chat_window.tag_config("code", background="#f4f4f4", font=("Courier", 10))
chat_window.tag_config("user", foreground="#004488", font=("Helvetica", 11, "bold"))
chat_window.tag_config("error", foreground="red")
chat_window.tag_config("normal", font=("Helvetica", 11))

# --- Load Previous Chat ---
history = load_history()
for msg in history:
    if msg["role"] == "user":
        chat_window.insert(tk.END, "You: " + msg["content"] + "\n", "user")
    elif msg["role"] == "assistant":
        insert_markdown(chat_window, "Assistant: " + msg["content"])
chat_window.insert(tk.END, "\n")
chat_window.see(tk.END)

# --- Start App ---
root.mainloop()
