from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TexttField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def___str___(self):
        return self.name

class Feedback(models.Model):
    comment = models.TexttField()
    created_at = model.DateTimeFIeld(auto_now_add=True)

    def___str___(self):
        return self.comment[:50]
class order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def___str___(self):
        return f"Order #{Self,id} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def___str___(self):
        return f"{self.quantity} x {self.menu_item.price}

def save(self, *args, **kwargs):
    self.total_amount = sum[(item.get_total_price() for item in self.items.all())] if self.id else 0
    super().save(*args, **kwargs)

python manage.py makemigrations
python manage.py migrate



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def___str___(self):
        return self.name


# Create your models here. 
