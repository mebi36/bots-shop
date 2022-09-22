from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api/v1/product/", include("product.urls")),
    path("api/v1/client/", include("client.urls")),
    path("api/v1/order/", include("order.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/api-auth/", include("rest_framework.urls")),
    path("api/v1/api-token-auth", obtain_auth_token, name='api-token-auth')
]
