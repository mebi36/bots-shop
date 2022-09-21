import os
from pathlib import Path
import json
from django.db.utils import IntegrityError

from client.models import Client
from product.models import Product
from order.models import Order

FIXTURE_DIR = os.path.join(Path(__file__).parent, "demodata")


def install_fixtures():
    print("Installing Client fixtures...", end='')
    with open(os.path.join(FIXTURE_DIR, "clients.json")) as datafile:
        clients = json.load(datafile)

    for client_obj in clients:
        password = client_obj["fields"].pop("password")
        try:
            new_client = Client.objects.create_user(**client_obj["fields"])
        except IntegrityError as e:
            print("\nError installing fixture: %s ...skipping" % e)
            continue
        new_client.set_password(password)
        new_client.save()

    print("Done")

    print("Installing Product fixtures...", end='')
    with open(os.path.join(FIXTURE_DIR, "products.json")) as datafile:
        products = json.load(datafile)

    for product_obj in products:
        try:
            Product.objects.create(**product_obj["fields"])
        except IntegrityError as e:
            print("\nError installing fixture: %s ...skipping" % e)
    print("Done")

    print("Installing order fixtures...", end='')
    with open(os.path.join(FIXTURE_DIR, "orders.json")) as datafile:
        orders = json.load(datafile)
        
    for order_obj in orders:
        try:
            Order.objects.create(**order_obj["fields"])
        except IntegrityError as e:
            print("\nError installing fixture: %s ...skipping" % e)
            continue
    print("Done")

    print("Fixture installation complete")