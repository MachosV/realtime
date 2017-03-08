from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Artist
from .consumers import notifyNewArtist

@receiver(pre_save, sender = Artist)
def new_artist(sender, instance, **kwargs):
    if instance._state.adding:
        notifyNewArtist(instance)

