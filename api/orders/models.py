from django.db import models
from api.core.models import BaseModel
from api.tables.models import Table
from api.menu.models import Menu

# Create your models here.


class OrderStatus(models.TextChoices):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class Order(BaseModel):
    table = models.ForeignKey(Table, on_delete=models.CASCADE , related_name="orders")
    status = models.CharField(
        max_length=255, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_customer = models.IntegerField()


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE , related_name="order_items")
    quantity = models.IntegerField()
