from django.db import models

class Forecast(models.Model):
    date = models.DateTimeField('forecast date')
    high_temp = models.IntegerField(default=0)
    low_temp = models.IntegerField(default=0)
