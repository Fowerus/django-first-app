from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Users


class UserRegistrationForm(UserCreationForm):

	class Meta:
		model = Users
		fields = ['login']



class UserLoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Users
		fields = ['login','password']