from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Phone,Log
from eos.consumers import notifyNewPhone,updatePhone
import datetime

def logNewPhone(instance):
    log = Log()
    log.imsi = instance.imsi
    log.field = "Created"
    log.value = instance.imsi
    log.timestamp = str(datetime.datetime.now())
    log.save()

@receiver(pre_save, sender = Phone)
def new_phone(sender, instance, **kwargs):
    if instance._state.adding:
        notifyNewPhone(instance)
        logNewPhone(instance)


