from django.db import models
from orders.models import Order


class Driver(models.Model):

    VEHICLE_CHOICES = [
        ('Bike', 'Bike'),
        ('Scooter', 'Scooter'),
        ('Car', 'Car'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    vehicle = models.CharField(
        max_length=20,
        choices=VEHICLE_CHOICES
    )

    experience = models.IntegerField()

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):

    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery {self.order.id}"