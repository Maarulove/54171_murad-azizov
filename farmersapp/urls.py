from django.urls import path
from . import views

urlpatterns = [
    
    path("accounts/", views.login_view, name="login" ),
    # path("home/", views.home, name="home"),
    # path("get_users   /", views.get_users, name="get_users"),
    
    path("categories/", views.categories, name="categories"),
    path("category_new/", views.create_category, name="category_new"),
    path("edit_category/<int:id>/", views.edit_category, name="edit_cat"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_cat"),

    path("my_areas/", views.my_areas, name="my_areas"),
    path("area_new/", views.create_area, name="area_new"),
    path("area_edit/<int:id>/", views.area_edit, name="area_edit"),
    path("delete_area/<int:id>/", views.delete_area, name="delete_area"),

    path("equipment/", views.equipments, name="equipment"),
    path("create_equipment/", views.create_equipment, name="create_equipment"),
    path("edit_equipment/<int:id>/", views.edit_equipment, name="edit_equipment"),
    path("delete_equipment/<int:id>/", views.delete_equipment, name="delete_equipment"),

    path("livestock_new/", views.create_livestock, name="livestock_new"),
    path("equipment_new/", views.create_equipment, name="equipment_new"),
    path("expense_new/", views.create_expense, name="expense_new"),
    path("income_new/", views.create_income, name="income_new"),
    path("home/", views.home, name="home"),
    path("register/", views.register, name="register"),


    path("weather/", views.Update_weather, name="weather"),
]
