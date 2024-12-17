from django.db import models

class users(models.Model):
    
    name_user = models.CharField(max_length=150, verbose_name="nombre", default="E_Silab")
    pass_user = models.CharField(max_length=100, verbose_name="codigo")
    rol_user = models.CharField(max_length=100, verbose_name="rol del usuario", default="null")
    

  