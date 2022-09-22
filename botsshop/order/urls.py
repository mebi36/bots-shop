from django.urls.conf import path

from .views import ClientOrderHistoryView

app_name = "order"

urlpatterns = [
    path("history/", ClientOrderHistoryView.as_view(), name="history"),
]
