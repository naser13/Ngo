from django.db import models
from django.contrib.auth.models import User
from news.models import News
from news.views import *


class Admin(models.Model):#modire site
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user.is_staff = True
        self.user.is_superuser = True

    def get_all_news(self):
        return News.objects.all()

    def get_all_new_news(self):
        return News.objects.filter(status='نا مشخص')



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
    continent = models.CharField(max_length=2,choices=CATEGORIES)
    title_picture = models.ImageField()
    Website = models.CharField(max_length=50)