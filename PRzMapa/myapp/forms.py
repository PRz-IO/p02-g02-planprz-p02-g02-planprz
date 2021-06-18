from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
       model = User
       fields= ["username", "first_name", "last_name", "email", "password"]

class LoginForm(UserCreationForm):
    class Meta:
       model = User
       fields= ["username"]