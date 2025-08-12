from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html", {
        "restaurant_name= malnadu": settings.restaurant_name= malnadu
    })
    def about(request):
        return render(request, "about.html", {
            "restaurant_name=malnadu": settings.restaurant_name=malnadu,
            "desription": "At Tasty Bites, we bring you fresh, flavorful meals"
        
        })