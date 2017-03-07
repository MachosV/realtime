from __future__ import unicode_literals

from django.db import models

class Modrei(models.Model):
    imsi = models.CharField(max_length = 16, primary_key = True)
    cipher_ind = models.BooleanField()
    kc = models.CharField()
    cipher_key = models.CharField(max_length = 8)
    integrity_key = models.CharField(max_length = 8)
    tmsi = models.CharField()
    tmsi_time = models.CharField()
    lai = models.CharField(max_length = 5)
    ptmsi = models.CharField()
    ptmsi_sign = models.CharField(max_length = 3)
    rai = models.CharField(max_length = 5)
    threshold = models.PositiveIntegerField()