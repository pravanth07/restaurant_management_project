from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'coupon code is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        try:
            coupon = Coupon.objects.get(code=code, is_active=True)
        except Coupon.DoesNotExist:
            return Response({'error': 'Invalid or inactive coupon code.'},
                            status=status.HTTP_400_BAD_REQUEST)
        today = timezone.now().date()
        if not (coupon.valid_from <= today <= coupon.valid_until):
            return Response({'error': 'Coupon is expired or not yet valid.'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': True,
            'discount_percentage': float(coupon.discount_percentage),
            'message': 'Coupon is valid.'
        },   status=status.HTTP_200_OK)
# Create your views here.
