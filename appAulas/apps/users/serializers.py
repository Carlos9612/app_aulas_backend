from rest_framework import serializers
from apps.users.models import users

class users_serializer(serializers.ModelSerializer):
  class Meta:
    model = users
    fields = ("id","name_user","pass_user","rol_user")
    
