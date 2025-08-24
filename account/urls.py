
from django.urls import path




urlpatterns = [
    path("admin/", admin.site.urls),
    
]
urlpatterns = [
    path("reservations/", views.reservations, name="reservations"),
    
]