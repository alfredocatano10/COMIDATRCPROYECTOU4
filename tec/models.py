from django.db import models

class memorias (models.Model):
	producto = models.CharField(default = "",null=True,max_length = 30)
	precio = models.IntegerField(default = "",null=True)
	marca = models.CharField(default = "",null=True,max_length = 30)
	modelo = models.CharField(default = "",null=True,max_length = 30)
	fecha = models.CharField(default = "",null=True,max_length = 20)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.producto

class monitores (models.Model):
	producto = models.CharField(default = "",null=True,max_length = 30)
	precio = models.IntegerField(default = "",null=True)
	marca = models.CharField(default = "",null=True,max_length = 30)
	modelo = models.CharField(default = "",null=True,max_length = 30)
	fecha = models.CharField(default = "",null=True,max_length = 20)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.producto

class teclados (models.Model):
	producto = models.CharField(default = "",null=True,max_length = 30)
	precio = models.IntegerField(default = "",null=True)
	marca = models.CharField(default = "",null=True,max_length = 30)
	modelo = models.CharField(default = "",null=True,max_length = 30)
	fecha = models.CharField(default = "",null=True,max_length = 20)
	imagen = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.producto

