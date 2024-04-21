from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth import get_user_model
# from django import forms

User = get_user_model()


class UserForm(ModelForm):
    password1 = CharField(label="Password", max_length=50, widget=PasswordInput())
    password2 = CharField(label="Password confirmation", max_length=50, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
