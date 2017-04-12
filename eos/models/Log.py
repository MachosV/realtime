from django.db import models

class Log(models.Model):
    imsi = models.CharField(max_length = 32, blank = False)
    field = models.CharField(max_length = 32)
    value = models.CharField(max_length = 32)
    timestamp = models.DateTimeField(blank = True, null = True)

class LogOrderedManager(models.Manager):
    def get_queryset(self):
        return super(LogOrderedManager,self).get_queryset().order_by("-timestamp")[:25]

class LogOrdered(Log):
    objects = LogOrderedManager()
    class Meta:
        proxy = True