from rest_framework import viewsets
from .models import HDDModel, CPUModel, GPUModel
from .serializers import HDDModelSerializer, GPUModelSerializer, CPUModelSerializer


class HDDModelViewSet(viewsets.ModelViewSet):
    queryset = HDDModel.objects.all()
    serializer_class = HDDModelSerializer


class CPUModelViewSet(viewsets.ModelViewSet):
    queryset = CPUModel.objects.all()
    serializer_class = CPUModelSerializer


class GPUModelViewSet(viewsets.ModelViewSet):
    queryset = GPUModel.objects.all()
    serializer_class = GPUModelSerializer
