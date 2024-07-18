import os
from django.db import models
from django.urls import reverse

from apps.categories.models import FishCategory
from utils.image_path import fish_upload


class Fish(models.Model):
    category = models.ForeignKey(
        FishCategory,
        on_delete=models.CASCADE,
        related_name='fishes',
        verbose_name="Категории рыб"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название рыбы"
    )
    description = models.TextField(
        verbose_name="Описание рыбки"
    )
    stock = models.PositiveIntegerField(
        default=0,
    )
    restock_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse(
            'product_detail',
            kwargs={"slug": self.slug}
        )

    def __str__(self):
        return self.name


class FishImage(models.Model):
    fish = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
        related_name='fish_images',
        verbose_name="Рыба"
    )
    image = models.ImageField(
        upload_to=fish_upload,
        verbose_name="Картинка рыбы"
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f'{self.fish.name}'

    class Meta:
        verbose_name = "Изображение Рыбы"
        verbose_name_plural = "Изображение Рыбы"
