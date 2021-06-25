from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import memorias, teclados, monitores

#-------------------------------------------------------------------
# FORMULARIOS DEL MODELO DE USUARIO PERSONALIZADO
#-------------------------------------------------------------------

class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#-------------------------------------------------------------------
# FORMULARIOS DE CADA MODELO
#-------------------------------------------------------------------

class memoriasForm (forms.ModelForm):
	
	class Meta:
		model = memorias
		fields = '__all__'

class tecladosForm (forms.ModelForm):
	
	class Meta:
		model = teclados
		fields = '__all__'

class monitoresForm (forms.ModelForm):
	
	class Meta:
		model = monitores
		fields = '__all__'
