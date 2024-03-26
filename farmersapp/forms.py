from django import forms
from .models import Users, Category, Income, Expense, Area, Livestock, Equipment, Login

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'email', 'phone', 'city', 'country']

        widgets = {
            "date_publish": forms.DateInput(attrs={"class": "form-control", "type":'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['def_name', 'slug', 'parent_category']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['user', 'description', 'amount', 'categories']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['user', 'description', 'amount']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'description', 'square', 'categories']

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['name', 'categories', 'description', 'quantity', 'money_spent']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['user', 'description']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']