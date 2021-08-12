from django.shortcuts import render
from .models import Ticket,Response
from .forms import TicketForm,ResponseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):
    context = {}
    return render(request,'ticket/home.html',context)

# ویو نشان دادن لیست تیکت های کاربر یا پشتیبان
@login_required
def TicketList(request):    
     
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

# ویو ثبت تیکت
@login_required
def AddTicket(request):      
    
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

# ویو نشان دادن تیکت و پاسخ های آن
@login_required
def TicketDetail(request,id):       
    
    ticketdetail = Ticket.objects.get(id=id)
    response = Response.objects.filter(ticket=ticketdetail).order_by('-pb_date')
    
    context = {
        'ticketdetail':ticketdetail,
        'response':response,
       
    }

    return render(request,'ticket/detail.html',context)

# ویو ثبت پاسخ
@login_required
def ResponsePage(request,id):        

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