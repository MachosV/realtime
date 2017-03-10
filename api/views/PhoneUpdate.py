from eos.models import Phone
from api.serializers import PhoneSerializer
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from eos.consumers import updatePhone
from rest_framework.renderers import JSONRenderer

class PhoneUpdate(UpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    #renderer_classes = (JSONRenderer,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updatePhone(json.dumps(request.data))
        #create log
        return HttpResponse("Ok",status=200)

    def get_object(self):
        return Phone.objects.get(imsi = self.request.data['imsi'])
