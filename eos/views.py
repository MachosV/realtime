from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from .models import Artist
# Create your views here.

def Dashboard(request):
    return HttpResponse("Hello world")

class ArtistList(ListView):
    template_name = "artists.html"
    model = Artist
    context_object_name = "artists"