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
# Create your models here.
