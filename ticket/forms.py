from django.db.models import fields
from django.db.models.base import Model
from .models import Ticket, Response
from django.forms import ModelForm
# class TicketForm(forms.Form):
#     STATUS_CHOICES = (
# 		('d', 'پشتیبانی'),
# 		('p', "حسابداری"),
# 	)
#     title = forms.CharField(label='Your name', max_length=100,required=True)
#     sup_type = forms.ChoiceField(choices=STATUS_CHOICES)
#     email = forms.EmailField(disabled=True,max_length=100, required=False)
#     content = forms.CharField(widget=forms.Textarea,required=True)


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ['pb_date', 'status', 'user', 'response']


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['content', 'image', ]
