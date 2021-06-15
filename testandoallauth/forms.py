from django import forms
from django.db import models
from django.contrib.auth import get_user_model


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Qual seu nome?', widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome'}))
    email = forms.EmailField(max_length=130, label = 'Qual o seu email?')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.save()

