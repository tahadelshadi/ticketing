from rest_framework import serializers
from .serializers import TicketSerializer
from ticket.models import Ticket
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
# Create your views here.


class TicketList(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetail(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = ()