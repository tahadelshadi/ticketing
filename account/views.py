from django.shortcuts import render

# Create your views here.

def Signup(request):
    context={

    }
    return render(request,'account/signup.html',context)