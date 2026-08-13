from django.urls import path
from . import views

urlpatterns = [
    path("", views.delivery_status, name="delivery_status"),
]