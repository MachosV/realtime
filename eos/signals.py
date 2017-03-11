from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Phone
from eos.consumers import notifyNewPhone,updatePhone

@receiver(pre_save, sender = Phone)
def new_phone(sender, instance, **kwargs):
    if instance._state.adding:
        notifyNewPhone(instance)

