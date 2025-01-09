
from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    #add validation to ensure data integrity
    def clean(self):
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero.")
        if self.stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative.")

    def __str__(self):
        return self.name

