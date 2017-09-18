from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Profile


class NonAdminAccountForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'size':34,'placeholder':'email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'size':34,'placeholder':'password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'size':34,'placeholder':'confirm password'}))

	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')

class LoginForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'size':34,'placeholder':'email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'size':34,'placeholder':'password'}))
	class Meta:
		model = User
		fields = ('email', 'password1')
