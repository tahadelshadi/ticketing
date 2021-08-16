
from django.urls import path
from . import views

app_name='ticket'

urlpatterns = [
    
    path('', views.Home, name="homepage"),
    # Ticket
    path('add/', views.AddTicket, name="ticket-add"),
    path('list/', views.TicketList, name="ticket-list"),
    path('detail/<int:id>', views.TicketDetail, name="ticket-detail"),
    # Response
    path('response/<int:id>', views.AddResponse, name="response-add"),

]