from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django import forms
from .models import User 



class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class AuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'