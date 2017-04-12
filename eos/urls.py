from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name = 'dashboard'),
    url(r'^phone/(?P<imsi>[-\w]+)$', PhoneDetail.as_view(), name = 'phone_detail'),
    url(r'^phones$',PhoneList.as_view(), name = 'phone_list'),
    url(r'^apiguide$',APIGuide.as_view(),name = 'apiguide')
]
