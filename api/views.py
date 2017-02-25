from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from eos.models import Artist
from .serializers import ArtistSerializer
import json
from rest_framework.views import APIView

class ArtistListWeb(APIView):
    def get(self,request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArtistSerializer(data = request.data)
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
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data_dictionary = json.loads(request._stream.getvalue())
        serializer = ArtistSerializer(data = data_dictionary)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse("", status = status.HTTP_201_CREATED)
        return JSONResponse("", status = status.HTTP_400_BAD_REQUEST)