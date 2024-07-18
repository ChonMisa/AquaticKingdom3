from rest_framework import serializers
from apps.cart.models import Cart, Item, Order


class ItemSerializer(serializers.ModelSerializer):
    fish = serializers.StringRelatedField()  # Отображает строковое представление модели
    accessory = serializers.StringRelatedField()  # Отображает строковое представление модели
    ffood = serializers.StringRelatedField()  # Отображает строковое представление модели

    class Meta:
        model = Item
        fields = ['id', 'fish', 'accessory', 'ffood', 'quantity', 'cart']
        read_only_fields = ['id', 'cart']


class CartSerializer(serializers.ModelSerializer):
    items_cart = ItemSerializer(many=True, read_only=True)
    total_sum = serializers.ReadOnlyField(source='get_total_sum')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items_cart', 'total_sum']
        read_only_fields = ['id', 'user']


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)  # Использование вложенного сериализатора для подробной информации

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'created_at', 'updated_at', 'status', 'delivery_type']
        read_only_fields = ['id', 'created_at', 'updated_at', 'status']
