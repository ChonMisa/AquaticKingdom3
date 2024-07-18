from django.db import models
from django.contrib.auth import get_user_model
from apps.fish.models import Fish
from apps.accessories.models import Accessory
from apps.fish_food.models import FishFood

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"{self.user}"

    def get_total_sum(self):
        return sum(i.get_subtotal_sum() for i in self.items_cart.all())

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Item(models.Model):
    fish = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
        related_name='cart_items_fish',
        verbose_name="Рыбы",
        blank=True,
        null=True
    )
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.CASCADE,
        related_name='cart_items_accessory',
        verbose_name="Аксессуары",
        blank=True,
        null=True
    )
    ffood = models.ForeignKey(
        FishFood,
        on_delete=models.CASCADE,
        related_name='cart_items_ffood',
        verbose_name="Корм для рыбы",
        blank=True,
        null=True
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Количество"
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items_cart",
        verbose_name="Корзина"
    )

    def get_subtotal_sum(self):
        if self.fish:
            return self.quantity * self.fish.price
        elif self.accessory:
            return self.quantity * self.accessory.price
        elif self.ffood:
            return self.quantity * self.ffood.price
        else:
            return 0

    def check_stock(self):
        if self.fish:
            if self.fish.stock < self.quantity:
                restock_date = self.fish.restock_date or 'неизвестна'
                return f'Недостаточно товара: {self.fish.name}. Ожидаемая дата пополнения: {restock_date}'
        elif self.accessory:
            if self.accessory.stock < self.quantity:
                restock_date = self.accessory.restock_date or 'неизвестна'
                return f'Недостаточно товара: {self.accessory.title}. Ожидаемая дата пополнения: {restock_date}'
        elif self.ffood:
            if self.ffood.stock < self.quantity:
                restock_date = self.ffood.restock_date or 'неизвестна'
                return f'Недостаточно товара: {self.ffood.title}. Ожидаемая дата пополнения: {restock_date}'
        return None

    def update_stock(self):
        if self.fish:
            self.fish.stock -= self.quantity
            self.fish.save()
        elif self.accessory:
            self.accessory.stock -= self.quantity
            self.accessory.save()
        elif self.ffood:
            self.ffood.stock -= self.quantity
            self.ffood.save()

    def __str__(self):
        if self.fish:
            return f"Элемент корзины: {self.quantity} x {self.fish.name} (Рыба)"
        elif self.accessory:
            return f"Элемент корзины: {self.quantity} x {self.accessory.title} (Аксессуары)"
        elif self.ffood:
            return f"Элемент корзины: {self.quantity} x {self.ffood.title} (Корм для рыбы)"
        else:
            return "Элемент корзины"

    class Meta:
        verbose_name = "Элемент Корзины"
        verbose_name_plural = "Элементы Корзин"


class Order(models.Model):
    DELIVERY_CHOICES = (
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Item')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='pending')
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='delivery')
