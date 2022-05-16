from django.contrib import admin
from .models import Car
from .models import Book
from .models import Payment

# Register your models here.
admin.site.register(Car)
admin.site.register(Book)
admin.site.register(Payment)