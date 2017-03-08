from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'artists_web',ArtistListWeb.as_view()),
    url(r'artists',ArtistList),
    url(r'phones_web',PhoneListWeb.as_view()),
    url(r'phones',PhoneList),
]
