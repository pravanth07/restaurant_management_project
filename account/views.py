from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
class MenuView(APIView):
    def get(self, request):
        menu = [
            {"name": "Margherita Pizza", "description": "Classic cheese and tomato pizza", "price": 8.99},
            {"name": "Veggie Burger", "description": "Grilled veggie patty with lettuce and tomato", "price":7.49},
            {"name": "pasta Alfredo", "description": "Creamy Alfredo sauce with fettuccine pasta":10.99},
            {"name": "Caesar Salad", "description": "Fresh romaine lettuce with Caesar dressing","price":6.99},

        ]


def custom_404(request, exception):
    return render(request, "404.html", status=404)
    
return Response(menu)

def homepage(request):
    menu_items = Menu.objects.all()
    return render(request, "homepage.html", {"menu":menu_items})

def home(request):
    api_url = "http://127.0.0.1:8000/api/menu/"
    response = requests.get(api_url)
    menu_items = response.jscon() if response.status_code == 200 else []

    return render(request, "home.html", {"menu_items":menu_items})
    