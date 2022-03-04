from django.forms import ModelForm
from .models import UserDetail


class LoginForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ('username', 'password',)


class SignUpForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = ('username', 'fullname', 'email_id', 'password','age')
