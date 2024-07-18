from rest_framework import serializers
from apps.categories.models import FishCategory


class FCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FishCategory
        fields = ['id', 'name', 'parent', 'image']
