using Luke.Core.ViewModel;
using MvvmCross.Core.ViewModels;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Luke.Core
{
    public class AppStart : MvxNavigatingObject, IMvxAppStart
    {
        public void Start(object hint = null)
        {
            ShowViewModel<BaseViewModel>();
        }
    }
}
