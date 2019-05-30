from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput(),
		help_text='Exampel@gmail.com')
	class Meta:
		model = User 
		fields =  ('username', 'password1','password2' )
