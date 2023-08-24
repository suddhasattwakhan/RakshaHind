from django.db import models
from django.contrib.auth.models import User

class Crime(models.Model):
    location = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    description = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crime = models.ForeignKey(Crime, on_delete=models.CASCADE)