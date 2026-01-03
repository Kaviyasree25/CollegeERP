from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class NameLoginForm(AuthenticationForm):
    """
    Custom login form that uses 'name' field instead of 'username'
    """
    username = forms.CharField(
        label='Name',
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'autofocus': True,
            'id': 'id_name'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'id': 'id_password'
        })
    )
    
    error_messages = {
        'invalid_login': "Please enter a correct name and password. Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive.",
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Change the field name from username to name for better UX
        self.fields['username'].label = 'Name'
        self.fields['username'].help_text = 'Enter your full name (as registered)'


