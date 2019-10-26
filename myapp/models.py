from django.db import models

# Create your models here.
class Event(models.Model):
    eventname = models.CharField(max_length=200)
    time = models.CharField(max_length=300)
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.eventname