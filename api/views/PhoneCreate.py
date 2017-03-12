from rest_framework.generics import CreateAPIView
from eos.models import Phone
from api.serializers import PhoneSerializer

class PhoneCreate(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer