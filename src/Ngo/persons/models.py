from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


class Expert(AbstractUser):#karshenas
    # CATEGORIES = (
    #     ('as', 'آسیا'),
    #     ('er', 'اروپا'),
    #     ('am', 'آمریکا'),
    #     ('au', 'استرالیا و اقیانوسیه'),
    #     ('af', 'آفریقا'),
    # )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __init__(self):
        self.is_staff = True


class Admin(Expert):

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