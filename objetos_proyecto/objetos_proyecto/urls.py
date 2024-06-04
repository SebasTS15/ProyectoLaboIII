from django.contrib import admin
from django.urls import path, include
from proyecto_app.views import (
    CrearUsuario, CrearObjeto, actualizarObjeto, eliminarObjeto, detalleObjeto, listObject, detallesUsuarios, loginView, inicio, index
)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('proyecto/createUser/', CrearUsuario.as_view(template_name="proyecto/createUser.html"), name='createUser'),
    path('proyecto/infoUser/<int:pk>', detallesUsuarios.as_view(template_name="proyecto/infoUser.html"), name='infoUser'),
    path('proyecto/login/', loginView, name='login_user'), 
    path('proyecto/createObject', CrearObjeto.as_view(template_name="proyecto/createObject.html"), name='createObject'),
    path('', inicio, name='login'),
    path('proyecto/index', listObject.as_view(template_name='proyecto/index.html'), name='index'),
    path('proyecto/detalle/<int:pk>', detalleObjeto.as_view(template_name="proyecto/detalleObjeto.html"), name='detalleObjeto'),
    path('proyecto/editar/<int:pk>', actualizarObjeto.as_view(template_name="proyecto/editarObjeto.html"), name='editarObjeto'),
    path('proyecto/eliminar/<int:pk>', eliminarObjeto.as_view(), name='eliminarObjecto'),
]
