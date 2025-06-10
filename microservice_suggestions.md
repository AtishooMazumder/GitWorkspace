# Suggested Microservice Decomposition

---
Microservice: IdentityAccessService  
Purpose: Manages authentication, authorization, user accounts, external logins, two-factor authentication, password management, and related UI.  
Concern: BLL/UI  
Classes:
- AddPhoneNumber (WingtipToys/Account/AddPhoneNumber.aspx.cs)
- AddPhoneNumber (WingtipToys/Account/AddPhoneNumber.aspx.designer.cs)
- Confirm (WingtipToys/Account/Confirm.aspx.cs)
- Confirm (WingtipToys/Account/Confirm.aspx.designer.cs)
- ForgotPassword (WingtipToys/Account/Forgot.aspx.cs)
- ForgotPassword (WingtipToys/Account/Forgot.aspx.designer.cs)
- Lockout (WingtipToys/Account/Lockout.aspx.cs)
- Lockout (WingtipToys/Account/Lockout.aspx.designer.cs)
- Login (WingtipToys/Account/Login.aspx.cs)
- Login (WingtipToys/Account/Login.aspx.designer.cs)
- Manage (WingtipToys/Account/Manage.aspx.cs)
- Manage (WingtipToys/Account/Manage.aspx.designer.cs)
- ManageLogins (WingtipToys/Account/ManageLogins.aspx.cs)
- ManageLogins (WingtipToys/Account/ManageLogins.aspx.designer.cs)
- ManagePassword (WingtipToys/Account/ManagePassword.aspx.cs)
- ManagePassword (WingtipToys/Account/ManagePassword.aspx.designer.cs)
- OpenAuthProviders (WingtipToys/Account/OpenAuthProviders.ascx.cs)
- OpenAuthProviders (WingtipToys/Account/OpenAuthProviders.ascx.designer.cs)
- Register (WingtipToys/Account/Register.aspx.cs)
- Register (WingtipToys/Account/Register.aspx.designer.cs)
- RegisterExternalLogin (WingtipToys/Account/RegisterExternalLogin.aspx.cs)
- RegisterExternalLogin (WingtipToys/Account/RegisterExternalLogin.aspx.designer.cs)
- ResetPassword (WingtipToys/Account/ResetPassword.aspx.cs)
- ResetPassword (WingtipToys/Account/ResetPassword.aspx.designer.cs)
- ResetPasswordConfirmation (WingtipToys/Account/ResetPasswordConfirmation.aspx.cs)
- ResetPasswordConfirmation (WingtipToys/Account/ResetPasswordConfirmation.aspx.designer.cs)
- TwoFactorAuthenticationSignIn (WingtipToys/Account/TwoFactorAuthenticationSignIn.aspx.cs)
- TwoFactorAuthenticationSignIn (WingtipToys/Account/TwoFactorAuthenticationSignIn.aspx.designer.cs)
- VerifyPhoneNumber (WingtipToys/Account/VerifyPhoneNumber.aspx.cs)
- VerifyPhoneNumber (WingtipToys/Account/VerifyPhoneNumber.aspx.designer.cs)
- ApplicationUser (WingtipToys/Models/IdentityModels.cs)
- ApplicationDbContext (WingtipToys/Models/IdentityModels.cs)
- IdentityHelper (WingtipToys/Models/IdentityModels.cs)
- EmailService (WingtipToys/App_Start/IdentityConfig.cs)
- SmsService (WingtipToys/App_Start/IdentityConfig.cs)
- ApplicationUserManager (WingtipToys/App_Start/IdentityConfig.cs)
- ApplicationSignInManager (WingtipToys/App_Start/IdentityConfig.cs)
- Startup (WingtipToys/Startup.cs)
Justification: All classes relate to user authentication, management, and UI flows for login, registration, password reset, security, and account management. This is a core bounded context in DDD and can be safely carved out as a single microservice.

---

Microservice: ProductCatalogService  
Purpose: Provides browsing, filtering, display, and management of products and categories, including admin product CRUD.  
Concern: BLL/UI  
Classes:
- ProductList (WingtipToys/ProductList.aspx.cs)
- ProductList (WingtipToys/ProductList.aspx.designer.cs)
- ProductDetails (WingtipToys/ProductDetails.aspx.cs)
- ProductDetails (WingtipToys/ProductDetails.aspx.designer.cs)
- AdminPage (WingtipToys/Admin/AdminPage.aspx.cs)
- AdminPage (WingtipToys/Admin/AdminPage.aspx.designer.cs)
- Category (WingtipToys/Models/Category.cs)
- Product (WingtipToys/Models/Product.cs)
- AddProducts (WingtipToys/Logic/AddProducts.cs)
Justification: These classes handle all aspects of catalog management and browsing, including admin CRUD operations and public-facing product/category display, forming a clear product catalog bounded context.

---

Microservice: ShoppingCartService  
Purpose: Handles customer shopping cart operations including add, remove, update, display, and cart persistence.  
Concern: BLL/UI  
Classes:
- AddToCart (WingtipToys/AddToCart.aspx.cs)
- AddToCart (WingtipToys/AddToCart.aspx.designer.cs)
- ShoppingCart (WingtipToys/ShoppingCart.aspx.cs)
- ShoppingCart (WingtipToys/ShoppingCart.aspx.designer.cs)
- ShoppingCartActions (WingtipToys/Logic/ShoppingCartActions.cs)
- CartItem (WingtipToys/Models/CartItem.cs)
Justification: These classes form a focused bounded context for shopping cart operations, state management, and cart item data.

---

Microservice: OrderCheckoutService  
Purpose: Manages the checkout process, order creation, payment integration, and order detail persistence.  
Concern: BLL/UI  
Classes:
- CheckoutStart (WingtipToys/Checkout/CheckoutStart.aspx.cs)
- CheckoutStart (WingtipToys/Checkout/CheckoutStart.aspx.designer.cs)
- CheckoutReview (WingtipToys/Checkout/CheckoutReview.aspx.cs)
- CheckoutReview (WingtipToys/Checkout/CheckoutReview.aspx.designer.cs)
- CheckoutComplete (WingtipToys/Checkout/CheckoutComplete.aspx.cs)
- CheckoutComplete (WingtipToys/Checkout/CheckoutComplete.aspx.designer.cs)
- CheckoutCancel (WingtipToys/Checkout/CheckoutCancel.aspx.cs)
- CheckoutCancel (WingtipToys/Checkout/CheckoutCancel.aspx.designer.cs)
- CheckoutError (WingtipToys/Checkout/CheckoutError.aspx.cs)
- CheckoutError (WingtipToys/Checkout/CheckoutError.aspx.designer.cs)
- Order (WingtipToys/Models/Order.cs)
- OrderDetail (WingtipToys/Models/OrderDetail.cs)
- NVPAPICaller (WingtipToys/Logic/PayPalFunctions.cs)
- NVPCodec (WingtipToys/Logic/PayPalFunctions.cs)
Justification: These classes collectively implement the checkout workflow, order and payment logic, and PayPal API integration—a classic order/checkout bounded context.

---

Microservice: SitePresentationService  
Purpose: Provides shared site layout, master pages, navigational elements, and general non-domain-specific site pages (about, contact, error, etc).  
Concern: UI  
Classes:
- SiteMaster (WingtipToys/Site.Master.cs)
- SiteMaster (WingtipToys/Site.Master.designer.cs)
- Site_Mobile (WingtipToys/Site.Mobile.Master.cs)
- Site_Mobile (WingtipToys/Site.Mobile.Master.designer.cs)
- ViewSwitcher (WingtipToys/ViewSwitcher.ascx.cs)
- ViewSwitcher (WingtipToys/ViewSwitcher.ascx.designer.cs)
- About (WingtipToys/About.aspx.cs)
- About (WingtipToys/About.aspx.designer.cs)
- Contact (WingtipToys/Contact.aspx.cs)
- Contact (WingtipToys/Contact.aspx.designer.cs)
- _Default (WingtipToys/Default.aspx.cs)
- _Default (WingtipToys/Default.aspx.designer.cs)
- ErrorPage (WingtipToys/ErrorPage.aspx.cs)
- ErrorPage (WingtipToys/ErrorPage.aspx.designer.cs)
Justification: These classes are not domain-specific but provide overall presentation, layout, navigation, and basic informational pages—best grouped in a separate presentation-focused service.

---

Microservice: AdminRoleManagementService  
Purpose: Handles role creation, assignment, and admin user/role setup tasks.  
Concern: BLL  
Classes:
- RoleActions (WingtipToys/Logic/RoleActions.cs)
Justification: Although only one class, role management is often separated in DDD and microservice architectures for clarity and security boundaries.

---

Microservice: InfrastructureSupportService  
Purpose: Provides bootstrapping, configuration, routing, environment variable access, and environment abstraction.  
Concern: Utility/Shared  
Classes:
- Global (WingtipToys/Global.asax.cs)
- BundleConfig (WingtipToys/App_Start/BundleConfig.cs)
- RouteConfig (WingtipToys/App_Start/RouteConfig.cs)
- ServerConfig (WingtipToys/App_Start/ServerConfig.cs)
- HostingEnvironment (WingtipToys/App_Start/ServerConfig.cs)
- Startup (WingtipToys/App_Start/Startup.Auth.cs)
Justification: These classes are responsible for application startup, configuration, and infrastructure logic, and do not belong to any domain-specific context.

---

Microservice: PlatformIntegrationService  
Purpose: Provides helpers and formatters for cloud platform integration (Cloud Foundry, Azure, etc) and service credential management.  
Concern: Utility/Shared  
Classes:
- CFEnvironmentVariables (WingtipToys/Helper/CFHelper.cs)
- AzureSearchCredentials (WingtipToys/Helper/CFHelper.cs)
- AzureStorageCredentials (WingtipToys/Helper/CFHelper.cs)
- AzureCredentials (WingtipToys/Helper/CFHelper.cs)
- BasicMySQLConnectionStringFormatter (WingtipToys/Helper/CFHelper.cs)
- BasicSQLServerConnectionStringFormatter (WingtipToys/Helper/CFHelper.cs)
- BasicAzureMessageBusConnectionStringFormatter (WingtipToys/Helper/CFHelper.cs)
- BasicAzureStorageConnectionStringFormatter (WingtipToys/Helper/CFHelper.cs)
Justification: All classes are utility helpers for external platform integration and credential management, and are used infrastructure-wide.

---

Microservice: ExceptionLoggingService  
Purpose: Provides centralized exception logging and error utility features.  
Concern: Utility/Shared  
Classes:
- ExceptionUtility (WingtipToys/Logic/ExceptionUtility.cs)
Justification: Separating cross-cutting concerns like error handling aids maintainability and service clarity.

---

Microservice: DataAccessService  
Purpose: Provides Entity Framework persistence, seeding, and model context for products, categories, cart items, and orders.  
Concern: DAL  
Classes:
- ProductContext (WingtipToys/Models/ProductContext.cs)
- ProductDatabaseInitializer (WingtipToys/Models/ProductDatabaseInitializer.cs)
Justification: These classes manage database access, seeding, and context for the core domain entities—separation allows for clear data persistence boundaries.

---

**Notes:**
- Designer files are grouped with their code-behind counterparts for each UI class.
- Some domain logic (e.g., ShoppingCartActions) is grouped with the UI it supports to keep bounded contexts cohesive.
- Utility and infrastructure are separated to enable shared, cross-service usage and easier migration to .NET 8 Core patterns.
- Minor classes (like NVPCodec) are grouped with their main consumer for cohesion.

This grouping follows DDD best practices for bounded contexts, supports modular migration to microservices, and clearly distinguishes between UI, domain, infrastructure, and shared utility concerns.