from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()
    REQUIRED_FIELDS = ["years_of_experience"]

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="cooks")

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name}: {self.price}$"
