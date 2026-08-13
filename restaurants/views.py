from django.shortcuts import render

RESTAURANTS = [
    {"id": 1, "name": "Spice Garden", "cuisine": "Indian", "rating": 4.5, "img": "https://picsum.photos/400/300?random=1"},
    {"id": 2, "name": "Pasta Palace", "cuisine": "Italian", "rating": 4.7, "img": "https://picsum.photos/400/300?random=2"},
    {"id": 3, "name": "Burger House", "cuisine": "Fast Food", "rating": 4.3, "img": "https://picsum.photos/400/300?random=3"},
    {"id": 4, "name": "Sushi World", "cuisine": "Japanese", "rating": 4.8, "img": "https://picsum.photos/400/300?random=4"},
]


def restaurant_list(request):
    return render(request, "restaurants/list.html", {"restaurants": RESTAURANTS})