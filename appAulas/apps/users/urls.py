from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'users$', views.users_list.as_view()),
    re_path(r'users/(?P<pk>[0-9]+)$', views.users_Detail.as_view())
]