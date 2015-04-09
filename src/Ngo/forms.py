from django import forms
from src.Ngo.persons.models import Expert
from Ngo.news.models import News,Photo


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


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pic']
