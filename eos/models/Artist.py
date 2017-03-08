from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length = 30, primary_key = True)
    band = models.CharField(max_length = 20, default = " ")
    songs = models.IntegerField(default = 0)
    def __str__(self):
        return self.name+" "+self.band+" "+str(self.songs)

    def get_self(self):
        return self.name + " " + self.band + " " + str(self.songs)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Artist._meta.fields]