from eos.models import Artist
from api.serializers import ArtistSerializer
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from eos.consumers import updateArtist
from rest_framework.renderers import JSONRenderer

class ArtistUpdate(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updateArtist(json.dumps(request.data))
        #create log
        return HttpResponse("Ok",status=200)

    def get_object(self):
        return Artist.objects.get(name = self.request.data['name'])
