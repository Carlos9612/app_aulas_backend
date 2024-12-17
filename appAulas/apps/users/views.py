from django.shortcuts import render
# se importa del rest framewor librerias genericas 
from rest_framework import generics
# se importa la clase almacenada dentro del modelo 
from apps.users.models import users
# se importa la clase serializadora 
from apps.users.serializers import users_serializer
# se crean la vistas generias que ya estan configuradas y ya vienen por defecto en el rest framework 
# se añaden dos cosas, primero el objeto que se va a usar y la clase que va a serializar o atributos 
class users_list(generics.ListCreateAPIView):
  queryset = users.objects.all()
  serializer_class = users_serializer
# se crea una vista mas para los detalles 
class users_Detail(generics.RetrieveUpdateDestroyAPIView):
  queryset = users.objects.all()
  serializer_class = users_serializer