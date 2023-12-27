from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username")
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
