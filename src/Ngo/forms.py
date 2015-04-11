from django import forms
from django.contrib.auth.models import User
from src.Ngo.persons.models import Expert, Admin
from Ngo.news.models import News, Photo


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = Expert
        fields = ['username', 'password1', 'password2', 'email']


class AddArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.fields['text'].widget.attrs.update({'id': 'summernote'})

    class Meta:
        model = News
        fields = ['title', 'description', 'text', 'continent', 'title_image']


class AddPicForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pic']


class AddAdmin(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(AddAdmin, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password2 == password1:
            raise forms.ValidationError('گذرواژه و تکرار آن یکی نیست')
        return password1

    def save(self, commit=True):
        user = super(AddAdmin, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = True
        user.first_name = ''
        user.last_name = ''
        user.email = ''
        user.is_staff = False
        user.is_active = True
        if commit:
            user.save()
        return user


class AddExpert(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='رمز')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='تکرار')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(AddExpert, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if not password2 == password1:
            raise forms.ValidationError('گذرواژه و تکرار آن یکی نیست')
        return password1

    def save(self, commit=True):
        user = super(AddExpert, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = False
        user.first_name = ''
        user.last_name = ''
        user.email = ''
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user