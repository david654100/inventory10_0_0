from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator


alphanumeric = RegexValidator(r'^[0-9a-zA-z]*$', 'Only Letters and Numbers are allowed.')

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length = 32, validators=[alphanumeric])
    first_name = forms.CharField(max_length = 32, validators=[alphanumeric])
    last_name = forms.CharField(max_length = 32, validators=[alphanumeric])


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' , 'password1', 'password2' ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length = 32, validators=[alphanumeric])
    first_name = forms.CharField(max_length = 32, validators=[alphanumeric])
    last_name = forms.CharField(max_length = 32, validators=[alphanumeric])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
