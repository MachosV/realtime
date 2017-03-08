from __future__ import unicode_literals

from django.db import models

class Phone(models.Model):
    status_choices = (
        ('0','Not Registered'),
        ('1','Registered Home'),
        ('2','Not Registered, Searching'),
        ('3','Denied'),
        ('4','Unknown'),
        ('5','Registered Roaming'),
    )
    operator = models.Charfield(max_length = 20)
    signal_q = models.PositiveSmallIntegerField()
    reg_status = models.CharField(choices = status_choices)
    imsi = models.CharField(max_length = 16, primary_key = True)
    cipher_ind = models.BooleanField()
    kc = models.CharField()
    kc_gprs = models.CharField()
    cipher_key = models.CharField(max_length = 8)
    integrity_key = models.CharField(max_length = 8)
    tmsi = models.CharField()
    tmsi_time = models.CharField()
    lai = models.CharField(max_length = 5)
    ptmsi = models.CharField()
    ptmsi_sign = models.CharField(max_length = 3)
    rai = models.CharField(max_length = 5)
    threshold = models.PositiveIntegerField()