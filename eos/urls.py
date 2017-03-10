from django.conf.urls import url
from views import Dashboard,PhoneList

urlpatterns = [
    url(r'^dashboard',Dashboard),
    url(r'^phones',PhoneList.as_view()),
]
