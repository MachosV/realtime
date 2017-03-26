from django.conf.urls import url
from api.views import *

urlpatterns = [
    url(r'phones',PhoneList.as_view()),
    url(r'phone_update',PhoneUpdate.as_view()),
    url(r'phone_create',PhoneCreate.as_view()),
    url(r'logs/(?P<imsi>\w+)',LogList.as_view()),
]
