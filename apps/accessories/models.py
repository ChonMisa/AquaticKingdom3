import os
from django.db import models

from utils.image_path import accessories


class Accessory(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    stock = models.PositiveIntegerField(
        default=0,
    )
    restock_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    # image = models.ImageField(
    #     upload_to=accessories,
    #     verbose_name="Изображение",
    #     blank=True,
    #     null=True
    # )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Slug"
    )

    def __str__(self):
        return self.title


class AccessoryImage(models.Model):
    accessory = models.ForeignKey(
        Accessory,
        on_delete=models.CASCADE,
        related_name='accessory_images',
        verbose_name="Аксессуар"
    )
    image = models.ImageField(
        upload_to=accessories,
        verbose_name="Картинка аксессуара"
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f'{self.accessory.title}'

    class Meta:
        verbose_name = "Изображение аксессуара"
        verbose_name_plural = "Изображение аксессуара"
