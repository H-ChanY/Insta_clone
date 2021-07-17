from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as _LoginView, LogoutView as _LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required



def indexD(request):
    return render(request, 'indexD.html')

class SignupView(CreateView):
    template_name='signup.html'
    form_class = UserCreationForm
    model= get_user_model()
    
    def get_success_url(self):
        return '/dd/login/'
    
class LoginView(_LoginView):
    template_name='login.html'
    
    
class LogoutView(_LogoutView):
    template_name='logout.html'

class Profile(DetailView):
    pass 


@login_required
def testview(request):
    return render(request,'indexD.html')