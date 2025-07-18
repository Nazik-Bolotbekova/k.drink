from django.db import models


class DrinkCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        blank=True,
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Drink(models.Model):
    category = models.ForeignKey(
        DrinkCategory,
        on_delete=models.CASCADE,
        related_name='drinks'
    )
    name = models.CharField(
        max_length = 100,
        unique = True
    )
    description = models.TextField(
        max_length = 100
    )
    image = models.ImageField(
        upload_to = 'drinks',
        blank = True,
        null = True
    )
    price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2
    )
    volume = models.PositiveIntegerField(
        default = 0,
        null = False,
        blank = False

    )
    country = models.CharField(
        max_length = 100,
        unique = True
    )
    is_available = models.BooleanField(
        default = True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class Review(models.Model):
    email = models.EmailField()
    fio = models.CharField(
        max_length=100,
    )
    review = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"




