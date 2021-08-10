from django.urls import path
from rest_framework.serializers import as_serializer_error
from .views import *
app_name = "api"

urlpatterns = [
    path('ticket/',TicketList.as_view(),name="list"),
    path('ticket/<int:pk>/',TicketDetail.as_view(),name='detail')
]

