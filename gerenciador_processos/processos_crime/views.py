from rest_framework import viewsets
from .models import Processo
from .serializers import ProcessoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.generic.edit import CreateView
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import ProcessoForm

class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer

    @action(detail=False, renderer_classes=[TemplateHTMLRenderer])
    def list_processos(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'processos': serializer.data}, template_name='nome_do_template.html')

