from eos.models import Phone
from rest_framework import serializers

class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        timestamp = serializers.DateTimeField()
        fields = '__all__'
