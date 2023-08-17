from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-2 my-5',
                                                    'placeholder': 'Username'})
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-2 my-5',
                                                      'placeholder': 'Password'})
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-2 my-5',
                                                      'placeholder': 'Confirm Password'})
