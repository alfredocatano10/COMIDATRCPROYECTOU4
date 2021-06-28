from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

from django.conf import settings


class ComentariosManager(models.Manager):
	def filtro_por_instancia(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)    #TOMA NUESTRA CLASE DE MODELO Y DEVUELVE EL TIPO DE CONTENIDO A LA INSTANCIA DONDE SE REPRESENTA

#CREACION DEL MODELO COMENTARIO
''' class comentarios(models.Model):
	USUARIO = models.ForeignKey(settings.AUTH_USER_MODEL, default =1)
	texto = models.TextField(verbose_name = "ComentariO")

	content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	tiempo = models.DateTimeField(auto_now_add = True)  # Para tomar tiempo de cuando fue creado el comentario
	
	class Meta:
		ordering = ['-tiempo']   #Se busca acomodar los comentarios del mas reciente al mas antiguo en existencia
'''


#CREACION DE TABLAS PARA LA BD
class lonches (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb


class gordas (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb

class tacos (models.Model):
	nomb = models.CharField(default = "",null=True,max_length = 50)
	descr = models.TextField(default = "",null=True,max_length = 500)
	date = models.CharField(default = "",null=True,max_length = 20)
	calif = models.CharField(default = "",null=True,max_length = 20)
	img = models.ImageField(upload_to = "imagen", null="True")

	def __str__ (self):
		return self.nomb



#SE REFERENCIA QUE EL COMENTARIO VA AL PRODUCTO DE GORDITAS
class Publicacion (models.Model):
	id = models.AutoField(primary_key = True)
	titulo = models.CharField(default="",null = False, max_length = 50)
	textoP = models.CharField(default="",null = False, max_length = 300)

	gordasc = models.ForeignKey(gordas, on_delete = models.CASCADE)
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)


class Meta:
	Permission = [('permiso_desde_codigo','este_es_un_permiso _reado_desde_codigo')]
