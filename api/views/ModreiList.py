from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from eos.models import Modrei
from api.serializers import ModreiSerializer
import json
from rest_framework.views import APIView

class ModreiListWeb(APIView):
    def get(self,request):
        modrei_objects = Modrei.objects.all()
        serializer = ModreiSerializer(artists, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ModreiSerializer(data = request.data)
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
def ModreiList(request):
    if request.method == 'GET':
        modrei_objects = Modrei.objects.all()
        serializer = ModreiSerializer(artists, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data_dictionary = json.loads(request._stream.getvalue())
        serializer = ModreiSerializer(data = data_dictionary)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse("", status = status.HTTP_201_CREATED)
        return JSONResponse("", status = status.HTTP_400_BAD_REQUEST)