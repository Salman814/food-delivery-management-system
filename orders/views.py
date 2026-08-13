from django.shortcuts import render, redirect


def cart(request):
    if request.method == "POST":
        return redirect("dashboard")
    return render(request, "orders/cart.html")