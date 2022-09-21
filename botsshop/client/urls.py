from django.urls.conf import path

from .views import ClientCreationView, ClientView

app_name = "client"

urlpatterns = [
    path("new/", ClientCreationView.as_view()),
    path("<int:pk>/", ClientView.as_view())
]
