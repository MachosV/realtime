from django.views.generic.detail import DetailView
from eos.models import Phone,Log

class PhoneDetail(DetailView):
    model = Phone
    context_object_name = "phone"
    template_name = "phone_detail.html"
    pk_url_kwarg = "imsi"

    def get_context_data(self, **kwargs):
        context = super(PhoneDetail,self).get_context_data(**kwargs)
        context['logs'] = Log.objects.filter(imsi = self.object.imsi)
        return context
