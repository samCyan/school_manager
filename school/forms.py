# users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import School

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = School
        fields = ('username', 'email', 'name', 'board')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = School
        fields = ('username', 'email', 'name', 'board')