from django.db import models

class UserManager(models.Manager):
    pass

# Create your models here.
class User(models.Model):

    id_user = models.AutoField(primary_key=True,editable=False)
    username = models.CharField(max_length=100, blank=False,null=False,editable=True)
    email = models.EmailField(max_length=200,default="ejemplo@gmail.com",editable=True,null=True, blank=False)
    password = models.CharField(max_length=50,unique=True,editable=True,null=False,blank=False,default='DEFAULT VALUE')
    phone = models.IntegerField(editable=True,null=False, blank=False)
    sexo = models.CharField(max_length=1,default=" ",blank=True,null=True)
    last_login = models.DateTimeField(auto_created=True,null=True,blank=True)
    date_joined = models.DateTimeField(auto_created=True,null=True,blank=True)
    objects = UserManager() 

    def getDate(self):
        return self.username, self.password
    

class Objeto(models.Model):
    id_objeto = models.AutoField(primary_key=True,editable=False)
    nombre_objeto = models.CharField(max_length=100)
    cantidad_objeto = models.IntegerField()
    tipo_objeto = models.CharField(max_length=100)
    lugar_perdiad = models.CharField(max_length=100, blank=False, null=False, default='DEFAULT VALUE')
    img = models.FileField()

class Edificio(models.Model):
    id_edificio = models.AutoField(primary_key=True,editable=False)
    nombre_edificio = models.CharField(max_length=50,default="Cedro/Lago/Cafeteria")
    id_objeto_edificio = models.ForeignKey(Objeto,on_delete=models.CASCADE,null=True)

class Meta:
    user_db = "usuario"
    objeto_db = "objeto"