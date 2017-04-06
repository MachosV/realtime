from django.views.generic.detail import DetailView
from eos.models import Phone,Log

class PhoneDetail(DetailView):
    model = Phone
    context_object_name = "phone"
    template_name = "phone_detail.html"
    pk_url_kwarg = "imsi"
