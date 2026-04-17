from django.db import models
from api.core.models import BaseModel
from api.category.models import Category


# Create your models here.
class Menu(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="menus")

    def __str__(self):
        return self.name
