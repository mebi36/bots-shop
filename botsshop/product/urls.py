from django.urls.conf import path

from product.views import ProductListCreateView

app_name = "product"

urlpatterns = [
    path("all/", ProductListCreateView.as_view(), name='list-create'),
]
