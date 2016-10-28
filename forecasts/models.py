import datetime

from django.db import models
from django.utils import timezone

class Forecast(models.Model):
    label = models.CharField(max_length=200,default='')
    date = models.DateTimeField('forecast date')
    high_temp = models.IntegerField(default=0)
    low_temp = models.IntegerField(default=0)

    def __str__(self):
        return self.label

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
