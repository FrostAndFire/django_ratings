from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
