from django.contrib import admin
from .models import Driver, Delivery


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'vehicle',
        'experience',
        'available',
    )


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'driver',
        'assigned_date',
    )