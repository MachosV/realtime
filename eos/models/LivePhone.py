from django.db import models
from eos.models import Phone

class LivePhone(models.Model):
    phone = models.OneToOneField(Phone,primary_key=True)

    def __str__(self):
        return self.phone.imsi+" "+self.phone.operator