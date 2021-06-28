from django.contrib import admin
from django.contrib.auth.models import Permission    #CLASE QUE GESTIONA LOS PERMISOS QUE TIENE DJANGO
from django.contrib.contenttypes.models import ContentType
from .models import tacos, lonches, gordas, Publicacion


#AGREGAMOS LAS TABLAS DE LA BD EN EL SITIO WEB
modelos = tacos, lonches, gordas

admin.site.register(modelos)
admin.site.register(Permission)      #CON ESTO SE AGREGA AL ADMIN DE DJANGO
admin.site.register(ContentType)