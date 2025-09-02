
from django.urls import path
from .views import MenuView



urlpatterns = [
    path("admin/", admin.site.urls),
    
]
urlpatterns = [
    path("reservations/", views.reservations, name="reservations"),
    
]
urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]