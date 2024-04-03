from django.urls import path
from . import views
from farmersapp import views as farmersapp_views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('profile/', farmersapp_views.home, name='home'),

]