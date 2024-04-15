from django.shortcuts import render
from .models import *

def home(request):
    template='dashboard/home.html'
    products = Product.objects.all()
    products=products[:100]
    context={
        'products':products
    }
    return render(request,template,context)