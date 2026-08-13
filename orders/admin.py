from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'restaurant',
        'menu_item',
        'quantity',
        'total_price',
        'status',
        'order_date',
    )