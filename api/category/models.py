from django.db import models
from api.core.models import BaseModel

# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
