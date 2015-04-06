from django import forms
from news.models import *
from persons.models import *
from news.models import *


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Expert
        fields = ['username', 'password1', 'password2', 'email']


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'text', 'continent', 'title_image']