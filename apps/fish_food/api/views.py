from rest_framework import viewsets
from apps.fish_food.models import FishFood
from apps.fish_food.api.serializers import FishFoodSerializer


class FishFoodViewSet(viewsets.ModelViewSet):
    queryset = FishFood.objects.all()
    serializer_class = FishFoodSerializer
