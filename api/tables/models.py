from django.db import models
from api.core.models import BaseModel
from api.branch.models import Branch
# Create your models here.

class TableStatus(models.TextChoices):
    AVAILABLE = 'available'
    OCCUPIED = 'occupied'

class Table(BaseModel):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=TableStatus.choices, default=TableStatus.AVAILABLE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)