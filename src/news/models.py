from django.db import models
from persons.models import Expert, Person


class New(models.Model):
    author = models.ForeignKey(Expert)


class Comment(models.Model):
    new = models.ForeignKey(New)
    author = models.ForeignKey(Person)