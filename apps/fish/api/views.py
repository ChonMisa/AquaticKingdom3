from rest_framework import viewsets, filters


from django_filters import rest_framework
from apps.fish.models import Fish

from .serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'name': ['icontains'],
        'category__name': ['icontains'],
        'price': ['gte', 'lte'],
    }
    search_fields = ['name', 'category__name', 'price', 'slug']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
