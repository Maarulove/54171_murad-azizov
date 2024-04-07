from django import forms
from django.contrib.auth.models import User
from .models import Users, Category, Income, Expense, Area, Livestock, Equipment, Login
from django_select2.forms import ModelSelect2MultipleWidget, Select2MultipleWidget
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm





class UserForm(forms.ModelForm):
    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
            username
            and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username
    # class Meta:
    #     model = User
    #     fields = ['phone', 'avatar']

    #     widgets = {
    #         "date_publish": forms.DateInput(attrs={"class": "form-control", "type":'date'}),
    #     }


class SignUpForm(UserCreationForm):
                 email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
                 class Meta:
                     model = User
                     fields = ('username', 'email', 'password1', 'password2')






class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['def_name', 'slug', 'parent_category']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["amount",
                  "description",
                  'categories'
                  ]
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount of expense'}),
            'description': forms.TextInput(attrs={'placeholder': 'where did you spend money?'}),
            }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["amount",
                  "description",
                  'categories'
                  ]
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter amount of expense'}),
            'description': forms.TextInput(attrs={'placeholder': 'where did you spend money?'}),
            }


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['location','name', 'square', 'price', 'categories', 'description',]
        # categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
        #                                              widget=ModelSelect2MultipleWidget(attrs={'placeholder': 'Select categories'}))

        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'square': forms.NumberInput(attrs={'placeholder': 'Enter square'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            # 'categories': Select2MultipleWidget(attrs={'placeholder': 'Select categories'}),
            # 'categories': ModelSelect2MultipleWidget(attrs={'data-placeholder': 'Select categories'}),

            'description': forms.TextInput(attrs={'placeholder': 'Short description (optional)'}),
        }

        
class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['name', 'categories', 'description', 'quantity', 'money_spent']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity'}),
            'money_spent': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'description': forms.TextInput(attrs={'placeholder': 'Short description (optional)'}),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'categories', 'description']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']