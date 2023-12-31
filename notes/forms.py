from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


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
