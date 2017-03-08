from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length = 30, primary_key = True)
    band = models.CharField(max_length = 20, default = " ")

    def __str__(self):
        return self.name+" "+self.band