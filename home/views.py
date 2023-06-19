from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    success_url = 'home/logout'
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    
    def get_success_url(self):
        return '/smart/notes'
    
    def login_view(request):
        return redirect('home:login')

#class based views
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

# class AuthorizedView(LoginRequiredMixin,TemplateView):
#     template_name = 'home/authorized.html'
#     login_url = '/admin'
    
