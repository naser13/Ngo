from django.db import models
from persons.models import Expert, NGO


class News(models.Model):
    Categories = (
        ('n', 'نامشخص'),
        ('i', 'مهم'),
        ('r', 'معمولی'),
    )

    status = models.CharField(default='n', max_length=1, choices=Categories)
    author = models.ForeignKey(Expert)
    date = models.DateField(auto_now_add=True) #have to change to jalali calender
    text = models.TextField() #It is better for text to be as a text file because the valume of the text is alot
    description = models.CharField(max_length=100)
    ngo = models.ForeignKey(NGO)


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
