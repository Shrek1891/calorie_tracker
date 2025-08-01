from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name


class Consumed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

