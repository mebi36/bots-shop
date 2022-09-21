from django.urls.conf import path

from product.views import ProductListView

app_name = "product"

urlpatterns = [
    path("all/", ProductListView.as_view()),
]
