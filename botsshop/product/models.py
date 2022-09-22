from django.db import models
from django.utils import timezone


class Product(models.Model):
    """This is the model for products."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now())
    available_qty = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "description"], name="duplicate_product"
            )
        ]

    def __str__(self):
        return self.name
