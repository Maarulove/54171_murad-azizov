from django import forms
from .models import Users,  Equipment, Expense, Income


class UserForm(forms.ModelForm):
    class meta:
        model = Users
        # fields = ['name', 'surname', 'email']
        fields = '__all__'

        widgets = {
            "date_publish": forms.DateInput(attrs={"class": "form-control", "type":'date'}),
        }


