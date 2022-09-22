from django.urls.conf import path

from .views import ClientCreationView, ClientView

app_name = "client"

urlpatterns = [
    path("create/", ClientCreationView.as_view(), name="create"),
    path("<int:pk>/", ClientView.as_view(), name="details"),
]
