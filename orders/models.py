from django.db import models
from .models import OrderStatus

class order(models.Model):
    # your existing fields...


    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def__str__(self):
        return f"order {self.id} - {self.status}"

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)


    def__str__(self):
        return self.name


# Create your models here.
