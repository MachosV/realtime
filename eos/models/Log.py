from django.db import models

class Log(models.Model):
    imsi = models.CharField(max_length = 32, blank = False)
    field = models.CharField(max_length = 32)
    value = models.CharField(max_length = 32)
    timestamp = models.DateTimeField(blank = True, null = True)