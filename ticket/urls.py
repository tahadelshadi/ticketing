
from django.urls import path
from . import views

app_name='ticket'

urlpatterns = [
    
    path('', views.Home, name="ticket-home"),
    path('list/', views.TicketList, name="ticket-list"),
    path('detail/<int:id>', views.TicketDetail, name="ticket-detail"),
    path('add/', views.AddTicket, name="ticket-add"),
    path('response/<int:id>', views.ResponsePage, name="response-add"),
]