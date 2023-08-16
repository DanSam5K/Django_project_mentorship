from django import forms
from django.core.exceptions import ValidationError

from .models import Notes, User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control mb-5 my-2"}),
            'password': forms.PasswordInput(attrs={"class": "form-control mb-5 my-2"}),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 5:
            raise ValidationError('Username is too short')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise ValidationError('Password is too short')
        return password


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control mb-5 my-2"}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5 my-2"}),
        }
        labels = {
            'title': 'Add a Title',
            'text': 'Write your thoughts here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('Title is too short')
        return title
