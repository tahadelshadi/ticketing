from django.shortcuts import render
from .models import Ticket,Response
from .forms import TicketForm,ResponseForm

# Create your views here.

def Home(request):
    context = {

    }
    return render(request,'ticket/home.html',context)


def TicketList(request):
     #ویو نشان دادن لیست تیکت های کاربریا پشتیبان
    ticket_list = Ticket.objects.all()
    sup_tickets = Ticket.objects.filter(sup_type='s')
    acc_tickets = Ticket.objects.filter(sup_type='a')
    cus_tickets = Ticket.objects.filter(user=request.user)

    context = {
        'tickets': ticket_list,
        'sup_tickets':sup_tickets,
        'acc_tickets':acc_tickets,
        'cus_tickets':cus_tickets,
    }
    return render(request,'ticket/list.html',context)

def AddTicket(request):
    # ویو ثبت تیکت
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
    else:
        form = TicketForm()

    context = {
        'form':form,
    }
    return render(request,'ticket/add.html',context)

def TicketDetail(request,id):
    # ویو نشان دادن تیکت و پاسخ های آن
    ticketdetail = Ticket.objects.get(id=id)
    response = Response.objects.filter(ticket=ticketdetail).order_by('-pb_date')
    
    context = {
        'ticketdetail':ticketdetail,
        'response':response,
       
    }

    return render(request,'ticket/detail.html',context)



def ResponsePage(request,id):
    # ویو ثبت پاسخ 
    ticket = Ticket.objects.get(id=id)

    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid() and ticket.status :
            form = form.save(commit=False)
            form.user = request.user
            form.ticket = ticket
            form.save()
    else:
        form = ResponseForm()

    context = {
        'form':form,
    }
    return render(request,'ticket/response.html',context)