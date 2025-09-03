
from django.urls import path
from .views import MenuView
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    
]
urlpatterns = [
    path("reservations/", views.reservations, name="reservations"),
    
]
urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]
urlpatterns = [
    path("", views.home, name="home"),
]