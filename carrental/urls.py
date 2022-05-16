from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fleet',views.fleet,name='fleet'),
    path('offers',views.offers,name='offers'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('books',views.books,name='books'),
    path('display',views.display,name='display'),
    path('payment2',views.payment,name='payment2'),
    path('paymentpage',views.paymentpage,name='paymentpage'),
    path('thanks',views.thanks,name='thanks'),
]
