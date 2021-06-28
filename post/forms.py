from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import gordas, tacos, lonches

#FORMULARIOS DE C/ TABLA
class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class LonchesForm (forms.ModelForm):
	
	class Meta:
		model = lonches
		fields = '__all__'

class TacForm (forms.ModelForm):
	
	class Meta:
		model = tacos
		fields = '__all__'

class GordForm (forms.ModelForm):
	
	class Meta:
		model = gordas
		fields = '__all__'
