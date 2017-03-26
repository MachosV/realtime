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
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(",")
            self.queryset = Log.objects.filter(imsi=self.kwargs['imsi']).filter(reduce(lambda x, y: x | y, [Q(field=value) for value in fields]))
        else:
            self.queryset = Log.objects.filter(imsi=self.kwargs['imsi'])
        return self.queryset