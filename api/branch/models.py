from django.db import models
from api.core.models import BaseModel

# Create your models here.


class BranchStatus(models.TextChoices):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MAINTENANCE = "maintenance"


class Branch(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    status = models.CharField(
        max_length=255, choices=BranchStatus.choices, default=BranchStatus.ACTIVE
    )
