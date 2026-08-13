from django.db import models


class User(models.Model):

    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Restaurant', 'Restaurant'),
        ('Admin', 'Admin'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.full_name