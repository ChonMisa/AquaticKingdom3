from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.cart.models import Cart, Order
from apps.cart.api.serializers import CartSerializer, OrderSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @method_decorator(login_required, name='dispatch')
    @action(detail=False, methods=['post'], url_path='purchase')
    def purchase_items(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response(
                {'error': 'Корзина не найдена. Пожалуйста, убедитесь, что вы добавили товары в корзину.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if cart.items_cart.count() == 0:
            return Response(
                {'error': 'Ваша корзина пуста. Добавьте товары в корзину перед оформлением заказа.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        errors = []
        for item in cart.items_cart.all():
            stock_error = item.check_stock()
            if stock_error:
                errors.append(stock_error)

        if errors:
            return Response(
                {'errors': errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Создать заказ
        delivery_type = request.data.get('delivery_type', 'delivery')
        order = Order.objects.create(user=user, delivery_type=delivery_type)

        for item in cart.items_cart.all():
            order.items.add(item)
            item.update_stock()  # Обновление количества товара на складе

        # Очистить корзину
        cart.items_cart.all().delete()

        serializer = OrderSerializer(order)
        return Response(
            {'message': 'Ваш заказ успешно оформлен!', 'order': serializer.data},
            status=status.HTTP_201_CREATED
        )


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['patch'], url_path='update-status')
    def update_status(self, request):
        """Обновить статус заказа"""
        order = self.get_object()
        new_status = request.data.get('status')
        if new_status:
            order.status = status
            order.save()
            serializer = self.get_serializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Статус заказа не указан.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='user-orders')
    def user_orders(self, request):
        """Получить заказы текущего пользователя"""
        user = request.user
        orders = Order.objects.filter(user=user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
