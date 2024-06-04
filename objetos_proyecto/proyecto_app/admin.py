from django.contrib import admin
# Register your models here.
from .models import User

@admin.register(User)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'phone', 'sexo', 'last_login','date_joined')
