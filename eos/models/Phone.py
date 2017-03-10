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
    imsi = models.CharField(max_length=16, primary_key=True)
    operator = models.CharField(max_length = 20)
    signal_q = models.PositiveSmallIntegerField()
    reg_status = models.CharField(max_length = 1, choices = status_choices)
    cipher_ind = models.BooleanField()
    kc = models.CharField(max_length = 10)
    kc_gprs = models.CharField(max_length = 10)
    cipher_key = models.CharField(max_length = 8)
    integrity_key = models.CharField(max_length = 8)
    tmsi = models.CharField(max_length = 10)
    tmsi_time = models.CharField(max_length = 6)
    lai = models.CharField(max_length = 5)
    ptmsi = models.CharField(max_length = 3)
    ptmsi_sign = models.CharField(max_length = 3)
    rai = models.CharField(max_length = 5)
    threshold = models.PositiveIntegerField()

    def get_self(self):
        return self.imsi + " " + self.operator + " " + str(self.threshold)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Phone._meta.fields]