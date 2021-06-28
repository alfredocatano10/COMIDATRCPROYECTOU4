from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from django.conf import settings


#CREACION DE TABLAS PARA LA BD (LONCHES)
class lonches (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb

#CREACION DE TABLAS PARA LA BD (GORDAS)
class gordas (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb

#CREACION DE TABLAS PARA LA BD (TACOS)
class tacos (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb