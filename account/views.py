from django.shortcuts import render,redirect
from .forms import SignupForm , AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login , authenticate

def Signup(request):            

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)           
            form.is_staff = True
            messages.success(request, "ثبت نام با موفقیت انجام شد" )
            form.save()
            login(request, form)
            return redirect("ticket:homepage")
        else:
            messages.error(request, "ثبت نام ناموفق.اطلاعات وارد شده صحیح نیست")    
    else:
        form = SignupForm()

    context={
        'form':form,
    }
    return render(request,'account/signup.html',context)


def Login(request):

    if request.user.is_authenticated :
        return redirect("ticket:homepage")       
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
                    return redirect("ticket:homepage")
                else:
                    messages.error(request,"اطلاعات وارد شده صحیح نیست.")
            else:
                messages.error(request,"اطلاعات وارد شده صحیح نیست.")
        form = AuthenticationForm()
        
    context={
        'form':form,
    }
    return render(request,'account/login.html',context)

