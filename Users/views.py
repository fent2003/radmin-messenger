from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from messenger.utils import DataMixin
from Users.forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

@login_required
def profile(request):
    content = loader.get_template("profile.html")
    return HttpResponse(content.render({}, request))

@login_required
def logout_profile(request):
    logout(request)
    return redirect("profile")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class LoginUser(DataMixin, LoginView):
    template_name = 'login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('index')