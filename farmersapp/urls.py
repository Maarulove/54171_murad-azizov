from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login" ),
    # path("home/", views.home, name="home"),
    # path("get_users   /", views.get_users, name="get_users"),
    path("category_new/", views.create_category, name="category_new"),
    path("area_new/", views.create_area, name="area_new"),
    path("livestock_new/", views.create_livestock, name="livestock_new"),
    path("equipment_new/", views.create_equipment, name="equipment_new"),
    path("expense_new/", views.create_expense, name="expense_new"),
    path("income_new/", views.create_income, name="income_new"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("weather/", views.Update_weather, name="weather"),
]
