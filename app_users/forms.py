from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

from .models import Book, Student

class UserForm(ModelForm):
    password1 = CharField(label="Password", max_length=50, widget=PasswordInput())
    password2 = CharField(label="Password confirmation", max_length=50, widget=PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'hobbies']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            }),
            # 'hobbies': forms.Sele(attrs={
            #     'class': 'w-full border rounded border-gray-900 py-2 px-4 outline-0'
            # }),
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title']
         