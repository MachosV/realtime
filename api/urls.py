from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'artists_web',ArtistListWeb.as_view()),
    url(r'artists',ArtistList),
    url(r'modrei_web',ModreiListWeb.as_view()),
    url(r'modrei',ModreiList),
]
