from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    """
    This is the model for the client.
    It inherits from Django's AbstractUser class.
    """
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now())
    street = models.TextField("Street Address")
    city = models.CharField("City of Residence", max_length=255)
    state = models.CharField("State of Residence", max_length=255)
    country = models.CharField("Country of Residence", max_length=30)