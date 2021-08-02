from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PWapp import models


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=32, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'username': 'Ваш игровой никнейм',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }
        labels = {
            'username': 'Никнейм',
            'password1': 'Пароль',
            'password2': 'Подтвердите',
        }

class LogInForm(forms.Form):
    username = forms.CharField(max_length=32, label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class CreateListForm(forms.ModelForm):
    name = forms.CharField(max_length=128, label='Название')
    access = forms.ChoiceField(choices=models.List.ACCESS_CHOICES, widget=forms.Select)
    players = forms.ModelMultipleChoiceField(queryset=models.Player.objects.all(), widget=forms.SelectMultiple)

    class Meta:
        model = models.List
        fields = ('name', 'access', 'players')
        help_texts = {
            'name': 'Название',
        }
        labels = {
            'name': 'Название списка: ',
            'access': 'Кто может получить доступ?',
            'players': 'Выберите игроков: ',
        }
