from eos.models import Modrei
from rest_framework import serializers
class ModreiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modrei
        fields = '__all__'

