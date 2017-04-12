from rest_framework.generics import CreateAPIView
from eos.models import Phone
from api.serializers import PhoneSerializer
from rest_framework.renderers import JSONRenderer

class PhoneCreate(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    renderer_classes = (JSONRenderer,)
