from django.db import models
from django.utils import timezone

from client.models import Client
from product.models import Product


class PaymentMethodChoices(models.TextChoices):
    """An enum of available payment methods."""
    CARD = "CARD", "DEBIT CARD"
    PAYPAL = "PYPL", "PAYPAL"
    STRIPE = "STRP", "STRIPE"


class Order(models.Model):
    """This is the model for a client's order. """
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    payment_method = models.CharField(max_length=10, choices=PaymentMethodChoices.choices, default=PaymentMethodChoices.CARD)
    placed_on = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ["placed_on"]
        constraints = [
            models.UniqueConstraint(fields=["client", "product", "placed_on"], name="duplicate_order")
        ]

    def __str__(self):
        return f'Order number: {self.id}'
    
    def total_price(self):
        """
        A method to compute the total price a client paide for an order
        ."""
        return (self.product.price * self.quantity)
