from django.db import models
from users.models import User
from restaurants.models import Restaurant, MenuItem


class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    order_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.id}"