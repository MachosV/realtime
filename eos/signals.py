from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Phone,Log
from eos.consumers import notifyNewPhone,updatePhone,notifyDashboard
import datetime,json
from api.serializers import LogSerializer

def logNewPhone(instance):
    fields = instance.__dict__
    for field,value in fields.items():
        if value is None or field is "_state":
            continue
        log = Log()
        log.imsi = instance.imsi
        if field is "imsi":
            log.field = "Created"
            log.value = instance.imsi
        else:
            log.field = field
            log.value = value
        log.timestamp = str(datetime.datetime.now())
        log.save()

@receiver(pre_save, sender = Phone)
def new_phone(sender, instance, **kwargs):
    if instance._state.adding:
        notifyNewPhone(instance)
        logNewPhone(instance)

@receiver(pre_save, sender = Log)
def new_log(sender, instance, **kwargs):
    data = LogSerializer(instance).data
    data['type'] = 'log'
    data['imsi'] = instance.imsi
    notifyDashboard(json.dumps(data))


