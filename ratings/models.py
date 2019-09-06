from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    avg_rating = models.IntegerField(default=0, null=True, blank=True)

class Rating(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
