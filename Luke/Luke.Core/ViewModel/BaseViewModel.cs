using MvvmCross.Core.ViewModels;
using MvvmCross.Plugins.Messenger;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Luke.Core.ViewModel
{
    public class BaseViewModel : MvxViewModel, IDisposable
    {
        protected IMvxMessenger Messenger;
        public BaseViewModel(IMvxMessenger messenger)
        {
            this.Messenger = messenger;
        }
        public void Dispose()
        {
            throw new NotImplementedException();
        }
    }
}
