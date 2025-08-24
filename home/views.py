from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import menu_items
from django.conf import settings
# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html", {
        "RESTAURANT_NAME": settings.RESTAURANT_NAME
        "RESTAURANT_PHONE": settings.RESTAURANT_PHONE
    })
    def about(request):
        return render(request, "about.html", {
            "restaurant_name": settings.restaurant_name,
            "desription": "At Tasty Bites, we bring you fresh, flavorful meals"
        
        })
def menu_items(request):
    menu = [
        {"name": "pizza", "price": 10},
        {"name": "Burger", "price": 7},
        {"name": "pasta", "price":9},
        {"name": "salad", "price":5},
    ]
    return render(request, "menu.html", {"menu" : menu})
def menu_item_detail(request, item_id):
    try:
        item = get_object_or_404(MenuItem, id=item_id)
        return JsonResponse({
            "id": item.id,
            "name": item.name,
            "price": item.price
        })
    except MenuItem.DoesNotExist:
        return JsonResponse({"error": "Menu item not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": f"Unexpected error: {str(e)}"},status=500)
        