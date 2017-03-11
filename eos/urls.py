from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^dashboard', Dashboard, name = 'index'),
    url(r'^phone/(?P<imsi>[-\w]+)/', PhoneDetail.as_view(), name = 'phone_detail'),
    url(r'^phones',PhoneList.as_view(), name = 'phone_list'),
]
