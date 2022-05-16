from django.conf import settings
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

# Create your views here.

def index(request):
 
    return render(request, 'index.html')
    

def fleet(request):
    obj=Car.objects.all()
    return render(request,'fleet.html',{'obj':obj})


def offers(request):
    return render(request,'offers.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def books(request):
   if request.method == 'POST':
       name=request.POST['name']
       email=request.POST['email']
       pickup=request.POST['pickup']
       returnl=request.POST['returnl']
       pickd=request.POST['pickd']
       returnd=request.POST['returnd']
       phone=request.POST['phone']
       book=Book(name=name,email=email,pickup=pickup,returnl=returnl,pickd=pickd,returnd=returnd,phone=phone)
       book.save()
       messages.info(request,'Successfully Booked')
       return redirect('display')

      
def display(request):
    item=Book.objects.all()
    return render(request,'offers.html',{'item':item})

def payment(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        payment=Payment(firstname=firstname,email=email,address=address,city=city,state=state,zip=zip)
        payment.save()
        messages.info(request,'Payment Successfull')
        return redirect('/')

def payment2(request):
    if request.method=='POST':
        cardholdername=request.POST['cardholdername']
        date=request.POST['date']
        cvv=request.POST['cvv']
        cardnumber=request.POST['cardnumber']
        payment=Payment(cardholdername=cardholdername,date=date,cvv=cvv,cardnumber=cardnumber)
        payment.save()
        messages.info(request,'Payment Successfull')
        return redirect('/')

def paymentpage(request):
     return render(request,'payment.html')

def thanks(request):
    return render(request, 'thanks.html')

@csrf_exempt
def checkout(request):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Is8ocSDdd2UwZBTy8x03fUm',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )   

        return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })

@csrf_exempt
def stripe_webhook(request):

    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_Xj8wBk2qiUcjDEmYu5kfKkOrJCJ5UUjW'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)



    def index(request):
        return render(request, 'payment.html')