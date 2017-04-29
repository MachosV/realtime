from rest_framework.generics import ListAPIView
from eos.models import Log
from api.serializers import LogSerializer
from django.db.models import Q
from rest_framework.renderers import JSONRenderer

class LogList(ListAPIView):
    serializer_class = LogSerializer
    queryset = None
    renderer_classes = (JSONRenderer,)

    def get_queryset(self):
        self.queryset = []
        if 'imsi' in self.kwargs:
            return logs_imsi(self)
        return paginated(self.request)


def logs_imsi(data):
    fields = data.request.query_params.get('fields')
    if fields:
        fields = fields.split(",")
        queryset = Log.objects.filter(imsi=data.kwargs['imsi']).filter(
            reduce(lambda x, y: x | y, [Q(field=value) for value in fields]))
    else:
        queryset = Log.objects.filter(imsi=data.kwargs['imsi'])
    return queryset

def paginated(request):
    print request.GET["count"]
    return Log.objects.all().order_by("-timestamp")