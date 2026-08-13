from django.contrib import admin
from .models import DeliveryPrediction


@admin.register(DeliveryPrediction)
class DeliveryPredictionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'distance_km',
        'weather',
        'traffic_level',
        'vehicle_type',
        'predicted_delivery_time',
        'created_at',
    )

    list_filter = (
        'weather',
        'traffic_level',
        'vehicle_type',
    )