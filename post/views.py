from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from .models import gordas, tacos, lonches
from .forms import GordForm, LonchesForm, TacForm , CustomUserForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

class HomeView(ListView):
	model = tacos
	template_name = 'home.html'
	context_object_name = 'post_list'

class tacosView(ListView):
	model = tacos
	template_name = 'tacos.html'
	context_object_name = 'tacos_list'

class gordasView(ListView):
	model = gordas
	template_name = 'gordas.html'
	context_object_name = 'gordas_list'

class lonchesView(ListView):
	model = lonches
	template_name = 'lonches.html'
	context_object_name = 'lonches_list'

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#INICIAR SESION Y REGISTRAR USUARIO
class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = tacos
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registroUsuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def agregar_lonches (request):

	if request.method == "GET":
		form = LonchesForm()
	else:
		form = LonchesForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('lonches')
	return render(request, 'AGREGARLONCHES.html', {"form": form})


def eliminar_lonches (request, id):
	lon = get_object_or_404(lonches, id=id)
	lon.delete()

	return redirect(to = "lonches")


def modificar_lonches (request, id):

	lon = get_object_or_404(lonches, id=id)

	data = {
		'form': LonchesForm(instance=lon)
	}

	if request.method == "GET":
		form = LonchesForm()
	else:
		form = LonchesForm(request.POST,request.FILES, instance=lon)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('lonches')
	return render(request, 'modificar.html', data)


#-------------------------------------------------------------------------

def agregar_gordas (request):

	if request.method == "GET":
		form = GordForm()
	else:
		form = GordForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('gordas')
	return render(request, 'AGREGARGORDAS.html', {"form": form})


def eliminar_gordas (request, id):
	God = get_object_or_404(gordas, id=id)
	God.delete()

	return redirect(to = "gordas")


def modificar_gordas (request, id):

	God = get_object_or_404(gordas, id=id)

	data = {
		'form': GordForm(instance=God)
	}

	if request.method == "GET":
		form = GordForm()
	else:
		form = GordForm(request.POST,request.FILES, instance=God)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('gordas')
	return render(request, 'modificar.html', data)


#-------------------------------------------------------------------------

def agregar_tacos (request):

	if request.method == "GET":
		form = TacForm()
	else:
		form = TacForm(request.POST,request.FILES)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('tacos')
	return render(request, 'agregar.html', {"form": form})


def eliminar_tacos (request, id):
	Tac = get_object_or_404(tacos, id=id)
	Tac.delete()

	return redirect(to = "tacos")


def modificar_tacos (request, id):

	Tac = get_object_or_404(tacos, id=id)

	data = {
		'form': TacForm(instance=Tac)
	}

	if request.method == "GET":
		form = TacForm()
	else:
		form = TacForm(request.POST,request.FILES, instance=Tac)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('tacos')
	return render(request, 'modificar.html', data)


class GordasBusqueda(ListView):
	model = gordas
	template_name = 'GordasBusqueda.html'
	context_object_name = 'gordas_list'

	def get_queryset(self):
		Busq = self.request.GET.get('b')
		return gordas.objects.filter(Q(nomb__contains=Busq))
		
			

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
