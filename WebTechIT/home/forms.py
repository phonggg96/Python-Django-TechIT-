from django import forms
import itertools
from django.utils.text import slugify
from django.forms import ModelForm, PasswordInput
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
User = get_user_model()
from home.models import Comment, TinTuc

#class LoginForm(ModelForm):
#    class Meta:
#       model = User
#        fields = ("username", "password")

#        widgets ={
#           "password": PasswordInput()
#        }
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This user does not exits")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")
        if not user.is_active:
            raise forms.ValidationError("This user is not longer avtive")
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(ModelForm):
    first_name = forms.CharField(label='Firts Name')
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    confirm_password = forms.CharField(max_length=20, widget=PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")
        widgets = {
            "password": PasswordInput()
        }

    # Ghi đè phương thức kiểm tra input
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        confirm_password = clean_data.get("confirm_password")
        if not confirm_password == password:
            self.add_error("password", "Passwords are not match.")

    def save(self):
        user = super().save()
        user.set_password(self.cleaned_data["password"])
        user.save()

        return user


class CommnentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop("post", "")
        self.current_user = kwargs.pop("user", "")

        super(). __init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.current_user
        self.instance.home = self.home

        return super().save(commit=commit)

