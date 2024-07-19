from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.accessories.models import Accessory
from .serializers import AccessorySerializer, AccessoryImageSerializer


class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = [AccessorySerializer, AccessoryImageSerializer]
    filter_backends = (DjangoFilterBackend,)
