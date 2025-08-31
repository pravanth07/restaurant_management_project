from django.urls import path
from .views import *
from . import views
urlpatterns = [
    
]
urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
]
