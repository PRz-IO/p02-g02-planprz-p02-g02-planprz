from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
       model = User
       fields= ["username", "first_name", "last_name", "email"]
       labels={
           "username": "Login",
           "first_name": "Imię",
           "last_name": "Nazwisko",
           "email": "Mail",
           "id_password1": "Hasło",
           "id_password2": "Powtórz Hasło"
       }


class LoginForm(UserCreationForm):
    class Meta:
       model = User
       fields= ["username"]
       labels = {
           "username": "Login"
       }


class PunktForm(ModelForm):
    class Meta:
        model = Punkt
        fields = [
            "informacje",
            "nr_telefonu"
        ]
