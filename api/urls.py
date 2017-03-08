from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'artists',ArtistList.as_view()),
    url(r'artist_update',ArtistUpdate.as_view()),
    url(r'phones',PhoneListWeb.as_view()),
]
