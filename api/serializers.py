from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ticket.models import Ticket 
from django.contrib.auth.models import User


class TicketSerializer(serializers.ModelSerializer):
    class Meta :
        model = Ticket
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'