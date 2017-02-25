from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'artists_web',views.ArtistListWeb.as_view()),
    url(r'artists',views.artist_list),
]
