from __future__ import unicode_literals

from django.db import models
import json

class Phone(models.Model):

    imsi = models.CharField(max_length=16, primary_key = True)
    operator = models.CharField(max_length = 20, blank = True)
    signal_q = models.PositiveSmallIntegerField(blank = True, null = True)
    reg_status = models.CharField(max_length = 32, blank = True)
    #reg_status = models.CharField(max_length = 1, choices = status_choices)
    cipher_ind = models.NullBooleanField(blank = True, null = True)
    kc = models.CharField(max_length = 10, blank = True)
    kc_gprs = models.CharField(max_length = 10, blank = True)
    cipher_key = models.CharField(max_length = 8,blank = True)
    integrity_key = models.CharField(max_length = 8,blank = True)
    tmsi = models.CharField(max_length = 10,blank = True)
    tmsi_time = models.CharField(max_length = 6,blank = True)
    lai = models.CharField(max_length = 5,blank = True)
    ptmsi = models.CharField(max_length = 3,blank = True)
    ptmsi_sign = models.CharField(max_length = 3,blank = True)
    rai = models.CharField(max_length = 5,blank = True)
    threshold = models.PositiveIntegerField(blank = True, null = True)

    def __str__(self):
        return self.imsi

    def get_self(self):
        return json.dumps({"imsi":self.imsi})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Phone._meta.fields]