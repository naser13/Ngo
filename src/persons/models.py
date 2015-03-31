from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user.is_staff = True
        self.user.is_superuser = True


class Expert(models.Model):
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user.is_staff = True


class Person(models.Model):
    user = models.OneToOneField(User)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)