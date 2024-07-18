from rest_framework import viewsets
from apps.categories.models import FishCategory
from .serializers import FCategorySerializer


class FCategoryViewSet(viewsets.ModelViewSet):
    queryset = FishCategory.objects.all()
    serializer_class = FCategorySerializer
