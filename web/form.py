from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog,ProfileImg, Booking
from django.forms.widgets import Textarea, TextInput, EmailInput, DateInput, Select, NumberInput

from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserProfile(ModelForm):
    class Meta:
        model = ProfileImg
        fields = '__all__'
        exclude = ['user']


class Useredit(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class PostBlog(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['user']

class Booking(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['hotel', 'rate']
        check_in = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'} )) 
        widgets = {
            # 'check_in': DateInput(attrs={'class': 'required form-control date_pick'}),
            'count': NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Number of Adults'}),
        }