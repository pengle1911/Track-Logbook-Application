from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    workout = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    rest_day = models.BooleanField(default=False)
    race_day = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Progression(models.Model):
    event = models.CharField(max_length=200)
    record = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.event
