from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from eos.models import Phone
from api.serializers import PhoneSerializer
import json
from rest_framework.views import APIView

class PhoneListWeb(APIView):
    def get(self,request):
        phone_objects = Phone.objects.all()
        serializer = PhoneSerializer(artists, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PhoneSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse("", status=status.HTTP_201_CREATED)
        return JSONResponse("", status=status.HTTP_400_BAD_REQUEST)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def PhoneList(request):
    if request.method == 'GET':
        phone_objects = Phone.objects.all()
        serializer = PhoneSerializer(artists, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data_dictionary = json.loads(request._stream.getvalue())
        serializer = PhoneSerializer(data = data_dictionary)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse("", status = status.HTTP_201_CREATED)
        return JSONResponse("", status = status.HTTP_400_BAD_REQUEST)