from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


class CustomUserForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "", "placeholder": ""})
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "user_type",
        )


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-field w-full p-3 border border-gray-300 rounded-lg",
                "placeholder": "Enter your username or email",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-field w-full p-3 border border-gray-300 rounded-lg",
                "placeholder": "Enter your password",
            }
        )
    )

    class Meta():
        model = CustomUser
        fields = ("email", "password")
