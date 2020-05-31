from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #if not mendetory then pass requiared = False, but default it is True. 

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']