from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from farmersapp.models import Users

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     phone = forms.CharField(max_length=20, required=False)
#     # avatar = forms.ImageField(required=False)
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'phone')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#         user_profile = Users.objects.create(user=user, phone=self.cleaned_data['phone'])
#         return user

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'phone')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Set email field
        if commit:
            user.save()
        return user





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