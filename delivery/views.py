from django.shortcuts import render


def delivery_status(request):
    return render(request, "delivery/status.html")