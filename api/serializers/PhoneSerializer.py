from eos.models import Phone
from rest_framework import serializers

class PhoneSerializer(serializers.ModelSerializer):

    reg_status = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = '__all__'

    def get_reg_status(self,obj):
        return obj.get_reg_status_display()
