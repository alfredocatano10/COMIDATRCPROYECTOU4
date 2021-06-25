from django.contrib import admin
from .models import memorias, monitores, teclados

model = memorias, monitores, teclados

admin.site.register(model)