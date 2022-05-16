from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('fleet')
        else:
            messages.info(request,'Invalid  Crediantials')
            return redirect('login')


    else:
        return render(request,'login.html')
def register(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            subject = 'welcome to Vehicle rentals'
            message = "Thank you for registering in  Vehicle rental system hope you enjoy the shopping"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            request.session['email'] = email
            #return redirect('login')
            #return render(request, 'signup.html', value)
            print("user Created")
            return redirect('login')
        else:
            print('Password not matching.....')
            return redirect("/")
        return redirect('register')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request);
    return redirect('/')
def fleet(request):
     return render(request,'fleet.html')
