from django.db import models
from django.contrib.auth.models import User
from Ngo.settings import MEDIA_ROOT


class Admin(models.Model):#modire site
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user.is_staff = True
        self.user.is_superuser = True

    # def get_all_news(self):
    #     return News.objects.all()
    #
    # def get_all_new_news(self):
    #     return News.objects.filter(status='نا مشخص')
    #
    # def get_all_important_news(self):
    #     return News.objects.filter(satus='مهم')
    #
    # def get_all_regular_news(self):
    #     return News.objects.filter(status='معمولی')

    # def delete_news(self,id):
    #     return News.objects.re

    # def setstatus(self, number, status):


class Expert(models.Model):#karshenas
    CATEGORIES = (
        ('as', 'آسیا'),
        ('er', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )

    continent = models.CharField(max_length=2,choices=CATEGORIES)
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user.is_staff = True


class NGO (models.Model):
    name = models.CharField(max_length=100)
    CATEGORIES = (
        ('as', 'آسیا'),
        ('er', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )

    continent = models.CharField(max_length=2, choices=CATEGORIES)
    title_picture = models.FileField(upload_to=MEDIA_ROOT)
    Website = models.CharField(max_length=50)