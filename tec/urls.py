from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import monitoresPageViewBusq,tecladosPageViewBusq,memoriasPageViewBusq,agregarMemorias,agregarMonitores,agregarTeclados,eliminarMemorias,eliminarMonitores,eliminarTeclados,modificarMemorias,modificarMonitores,modificarTeclados,tecladosPageView,memoriasPageView,monitoresPageView,password_reset_request,HomePageView,RegistroPageView,registro_usuario,changePassword

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('teclados/',tecladosPageView.as_view(), name = 'teclados'),
	path('memorias/',memoriasPageView.as_view(), name = 'memorias'),
	path('monitores/',monitoresPageView.as_view(), name = 'monitores'),
	path('modificarTeclados/<id>/',modificarTeclados, name = 'modificarTeclados'),
	path('eliminarTeclados/<id>/',eliminarTeclados, name = 'eliminarTeclados'),
	path('agregarTeclados/',agregarTeclados, name = 'agregarTeclados'),
	path('modificarMemorias/<id>/',modificarMemorias, name = 'modificarMemorias'),
	path('eliminarMemorias/<id>/',eliminarMemorias, name = 'eliminarMemorias'),
	path('agregarMemorias/',agregarMemorias, name = 'agregarMemorias'),
	path('eliminarMonitores/<id>/',eliminarMonitores, name = 'eliminarMonitores'),
	path('modificarMonitores/<id>/',modificarMonitores, name = 'modificarMonitores'),
	path('agregarMonitores/',agregarMonitores, name = 'agregarMonitores'),
	path('registration/registro_success',RegistroPageView.as_view(), name = 'registro_success'),
	path('registration/registrar', registro_usuario, name='registrar'),	
	path("password_reset", password_reset_request, name="password_reset"),
	path('change_password/', changePassword, name = 'change_password' ),
	path('busqMemo/', memoriasPageViewBusq.as_view(), name = 'busqMemo' ),
	path('busqMoni/', monitoresPageViewBusq.as_view(), name = 'busqMoni' ),
	path('busqTecl/', tecladosPageViewBusq.as_view(), name = 'busqTecl' ),
]