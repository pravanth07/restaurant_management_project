from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html", {
        "restaurant_name": settings.restaurant_name
    })
    def about(request):
        return render(request, "about.html", {
            "restaurant_name": settings.restaurant_name,
            "desription": "At Tasty Bites, we bring you fresh, flavorful meals"
        
        })