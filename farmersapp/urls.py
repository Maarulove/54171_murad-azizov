from django.urls import path
from . import views
from accounts import views as accounts_views 
app_name = "profile"
urlpatterns = [
    
    # path("accounts/", views.login_view, name="login" ),
    path("farmersapphome/", views.home, name="home"),
    path("", views.home, name="home"),
    path("logout/", accounts_views.logout_view, name="logout"),
    path("login/", accounts_views.login_view, name="login"),
    path("register/", accounts_views.signup, name="register"),
    
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

    path("livestock/", views.livestock, name="livestock"),
    path("livestock_new/", views.create_livestock, name="create_livestock"),
    path("edit_livestock/<int:id>/", views.edit_livestock, name="edit_livestock"),
    path("delete_livestock/<int:id>/", views.delete_livestock, name="delete_livestock"),

    path("incomes/", views.income, name="income"),
    path("income_new/", views.create_income, name="income_new"),
    path("edit_income/<int:id>/", views.edit_income, name="edit_income"),
    path("delete_income/<int:id>/", views.delete_income, name="delete_income"),

    path("expenses/", views.expense, name="expense"),
    path("expense_new/", views.create_expense, name="expense_new"),
    path("edit_expense/<int:id>/", views.edit_expense, name="edit_expense"),
    path("delete_expense/<int:id>/", views.delete_expense, name="delete_expense"),

    path("weather/", views.Update_weather, name="weather"),
]
