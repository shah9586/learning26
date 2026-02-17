from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name
