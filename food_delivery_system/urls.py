from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("restaurants/", include("restaurants.urls")),
    path("orders/", include("orders.urls")),
    path("delivery/", include("delivery.urls")),
    path("feedback/", include("feedback.urls")),
    path("promotions/", include("promotions.urls")),
    path("prediction/", include("prediction.urls")),
]