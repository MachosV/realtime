from django.views.generic.list import ListView
from eos.models import Phone

class PhoneList(ListView):
    template_name = "phones.html"
    model = Phone
    context_object_name = "phones"