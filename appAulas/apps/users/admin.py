from django.contrib import admin
from apps.users.models import users
# Register your models here.

class usersAdmin(admin.ModelAdmin):
    list_display = ("name_user","pass_user","rol_user")  
admin.site.register(users,usersAdmin)