from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from eos.models import Phone
from api.serializers import PhoneSerializer
import json
from rest_framework.views import APIView

class PhoneList(APIView):

    renderer_classes = (JSONRenderer,)

    def get(self,request):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PhoneSerializer(data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response("", status=status.HTTP_201_CREATED)
        return Response("", status=status.HTTP_400_BAD_REQUEST)