from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User, Objeto

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id_user
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        except ObjectDoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'proyecto/login_user.html')



def login_user(request):
    return render(request,'proyecto/login_user.html')

def inicio(request):
    return render(request,'proyecto/inicio.html')

def index(request):
    return render(request,'proyecto/index.html')

class ListadoUsuarios(ListView):
    model = User

class CrearUsuario(SuccessMessageMixin, CreateView): 
    model = User
    fields = ['username', 'phone', 'email', 'password', 'sexo']
    success_message = 'Usuario Creado Correctamente!' 

    def get_success_url(self):
        return reverse('login')

class actualizarUsuario(SuccessMessageMixin, UpdateView): 
    model = User
    form = User 
    fields = "__all__"  
    success_message = 'Usuario actualizado Correctamente!' 

    def get_success_url(self):
        return reverse('index')
    
class detallesUsuarios(DetailView):
    model = User

class eliminarUsuario(SuccessMessageMixin, DeleteView): 
    model = User
    form = User 
    fields = "__all__"  

    def get_success_url(self):
        success_message = 'Usuario eliminado Correctamente!'
        messages.success (self.request, (success_message)) 
        return reverse('index')



class listObject(ListView):
    model = Objeto


class CrearObjeto(CreateView,SuccessMessageMixin):
    model = Objeto
    form = Objeto 
    fields = "__all__" 
    success_message = "Objeto Creada Correctamente!"

    def get_success_url(self):
        return reverse('index') 

class actualizarObjeto(SuccessMessageMixin,UpdateView):
    model = Objeto
    form = Objeto
    fields = '__all__'
    success_message = "Objeto actualizado Correctamente!"

    def get_success_url(self):
        return reverse('index') 

class detalleObjeto(DetailView):
    model = Objeto

class eliminarObjeto(DeleteView,SuccessMessageMixin):
    model = Objeto
    form = Objeto 
    fields = "__all__" 

    def get_success_url(self):
        success_message = 'Usuario eliminado Correctamente!'
        messages.success (self.request, (success_message)) 
        return reverse('index')
    