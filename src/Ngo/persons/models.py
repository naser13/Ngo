from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


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
    #
    # def delete_news(self,id):
    #     return News.objects.re
    #
    # def setstatus(self, number, status):

class BaseUser(AbstractUser):

     class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Expert(BaseUser):#karshenas
    CATEGORIES = (
        ('as', 'آسیا'),
        ('er', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    continent = models.CharField(max_length=2, choices=CATEGORIES)

    def __init__(self):
        self.is_staff = True


class Admin(BaseUser):

    def __init__(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = True


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
    title_picture = models.FileField(upload_to=settings.MEDIA_ROOT)
    Website = models.CharField(max_length=50)