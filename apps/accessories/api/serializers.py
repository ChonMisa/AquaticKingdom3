from rest_framework import serializers
from apps.accessories.models import Accessory


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ['id', 'title', 'description', 'image', 'price', 'slug']
