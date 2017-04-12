from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from eos.models import LivePhone,LogOrdered

class Dashboard(ListView):
    model = LivePhone
    template_name = "dashboard.html"
    context_object_name = "live_phones"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['logs'] = LogOrdered.objects.all()
        return context