from django.views.generic.list import ListView
from eos.models import Phone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

#@method_decorator(cache_page(20), name='dispatch')
class PhoneList(ListView):
    template_name = "phones.html"
    model = Phone
    context_object_name = "phones"