from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class FishCategory(MPTTModel):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name='Категория'
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True,
        verbose_name="Картинка"
    )

    def __str__(self):
        return self.name

    def indented_name(self):
        return f"--- {self.name}"
