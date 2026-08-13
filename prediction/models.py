from django.db import models


class DeliveryPrediction(models.Model):

    distance_km = models.FloatField()

    weather = models.CharField(
        max_length=50
    )

    traffic_level = models.CharField(
        max_length=50
    )

    time_of_day = models.CharField(
        max_length=50
    )

    vehicle_type = models.CharField(
        max_length=50
    )

    preparation_time = models.IntegerField()

    courier_experience = models.IntegerField()

    predicted_delivery_time = models.FloatField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"Prediction {self.id}"