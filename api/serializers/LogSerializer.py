from eos.models import Log
from rest_framework import serializers

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = ("field","value","timestamp")


