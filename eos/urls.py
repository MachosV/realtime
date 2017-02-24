from django.conf.urls import url
from views import Dashboard,ArtistList

urlpatterns = [
    url(r'^dashboard',Dashboard),
    url(r'^artists',ArtistList.as_view()),
]
