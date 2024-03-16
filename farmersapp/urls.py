from django.urls import path
from . import views

urlpatterns = [
    path("", views.init, name="init" ),
    path("get_users/", views.get_users, name="get_users"),
]
