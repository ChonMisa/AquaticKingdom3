from rest_framework import serializers
from apps.accessories.models import Accessory, AccessoryImage


class AccessoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoryImage
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class AccessorySerializer(serializers.ModelSerializer):
    accessory_images = AccessoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Accessory
        fields = '__all__'
