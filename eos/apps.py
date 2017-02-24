from __future__ import unicode_literals

from django.apps import AppConfig


class EosConfig(AppConfig):
    name = 'eos'

    def ready(self):
        import eos.signals
