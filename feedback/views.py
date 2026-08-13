from django.shortcuts import render, redirect


def feedback(request):
    if request.method == "POST":
        return redirect("home")
    return render(request, "feedback/feedback.html")