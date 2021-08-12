from django.shortcuts import render,redirect
from .forms import SignupForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login , authenticate
# Create your views here.

#ثبت نام کاربر
def Signup(request):            

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)           
            form.is_staff = True
            messages.success(request, "ثبت نام با موفقیت انجام شد" )
            form.save()
            login(request, form)
            return redirect("ticket:ticket-home")
        else:
            messages.error(request, "ثبت نام ناموفق.اطلاععات وارد شده صحیح نیست")    
    else:
        form = SignupForm()

    context={
        'form':form,
    }
    return render(request,'account/signup.html',context)

#ورود کاربر
def Login(request):

    if request.user.is_authenticated :
        return redirect("ticket:ticket-home")
        
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("ticket:ticket-home")
                else:
                    messages.error(request,"Invalid username or password.")
            else:
                messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        
    context={
        'form':form,
    }
    return render(request,'account/login.html',context)


