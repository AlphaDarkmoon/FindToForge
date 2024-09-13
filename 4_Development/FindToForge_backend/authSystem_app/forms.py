# authSystem_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your last name.")
    username = forms.CharField(max_length=150, required=True, help_text="Required. Enter a username.")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

