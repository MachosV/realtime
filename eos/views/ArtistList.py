from django.views.generic.list import ListView
from eos.models import Artist

class ArtistList(ListView):
    template_name = "artists.html"
    model = Artist
    context_object_name = "artists"