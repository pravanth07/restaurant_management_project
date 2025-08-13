from django.contrib import admin
from django.urls import path


handler404 = "yourapp.views.custom_404"


urlpatterns = [
    path("admin/", admin.site.urls),
    
]