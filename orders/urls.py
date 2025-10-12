from django.urls import path
from .views import *
from . import views
urlpatterns = [
    
]
urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
]
urlpatterns = [
    path('coupons/validate/', CouponValidationView.as_view(), name='coupon-validate'),
    
]
urlpatterns