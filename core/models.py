from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """

    """
    text = models.TextField(null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    owner = models.ForeignKey(User)


class Answer(models.Model):
    """

    """
    text = models.TextField(null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    owner = models.ForeignKey(User)
