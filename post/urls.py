from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import GordasBusqueda, tacosView,gordasView,lonchesView,modificar_gordas,modificar_lonches,modificar_tacos,eliminar_gordas,eliminar_lonches,eliminar_tacos,agregar_gordas,agregar_lonches,agregar_tacos,password_reset_request,HomeView,RegistroPageView,registroUsuario,changePassword

#SE AGREGAN LAS RUTAS DE LA APLICACION (POST) Y SE IMPORTARON LAS VISTAS DE .view
urlpatterns = [
	path('',HomeView.as_view(),name = 'home'),
	path('registration/registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registration/registrar', registroUsuario, name='registrar'),	
	path('change_password/', changePassword, name = 'change_password' ),
	path("password_reset", password_reset_request, name="password_reset"),
	path("tacos", tacosView.as_view(), name="tacos"),
	path('modificar_tacos/<id>/',modificar_tacos, name = 'modificar_tacos'),
	path('eliminar_tacos/<id>/',eliminar_tacos, name = 'eliminar_tacos'),
	path('agregar/',agregar_tacos, name = 'agregar'),
	path("gordas", gordasView.as_view(), name="gordas"),
	path('modificar_gordas/<id>/',modificar_gordas, name = 'modificar_gordas'),
	path('eliminar_gordas/<id>/',eliminar_gordas, name = 'eliminar_gordas'),
	path('AGREGARGORDAS/',agregar_gordas, name = 'AGREGARGORDAS'),
	path("lonches", lonchesView.as_view(), name="lonches"),
	path('modificar_lonches/<id>/',modificar_lonches, name = 'modificar_lonches'),
	path('eliminar_lonches/<id>/',eliminar_lonches, name = 'eliminar_lonches'),
	path('AGREGARLONCHES/',agregar_lonches, name = 'agregar'),
	path('GordasBusqueda/', GordasBusqueda.as_view(), name = 'GordasBusqueda'),
]