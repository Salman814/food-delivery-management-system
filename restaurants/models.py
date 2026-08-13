from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.food_name