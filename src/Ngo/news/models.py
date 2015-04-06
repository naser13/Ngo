from django.db import models
from src.Ngo.settings import MEDIA_ROOT


class News(models.Model):
    Categories = (
        ('n', 'نامشخص'),
        ('i', 'مهم'),
        ('r', 'معمولی'),
    )
    CATEGORIES = (
        ('as', 'آسیا'),
        ('er', 'اروپا'),
        ('am', 'آمریکا'),
        ('au', 'استرالیا و اقیانوسیه'),
        ('af', 'آفریقا'),
    )
    title = models.CharField(max_length=50)
    continent = models.CharField(max_length=2, choices=CATEGORIES)
    status = models.CharField(default='n', max_length=1, choices=Categories)
    date = models.DateField(auto_now_add=True) #have to change to jalali calender
    text = models.TextField() #It is better for text to be as a text file because the valume of the text is alot
    description = models.CharField(max_length=100)
    title_image = models.FileField(upload_to=MEDIA_ROOT)
    random_int = models.IntegerField()


class Comment(models.Model):
    time = models.DateTimeField(auto_now_add=True)#needs to be jalali datetime
    news = models.ForeignKey(News)
    name = models.CharField(max_length=50)
    text = models.TextField()


class Answer(models.Model):
    time = models.DateTimeField(auto_now_add=True)#jalali datetime
    comment = models.ForeignKey(Comment)
    name = models.CharField(max_length=20)
    text = models.TextField()