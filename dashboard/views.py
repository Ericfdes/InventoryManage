from django.shortcuts import render
from .models import *




def home(request):
    template='dashboard/home.html'
    products = Product.objects.all()
    products=products[:100]
    overview_data = Product.inventory_overview()
    print(overview_data)
    print()
    sales=Product.total_sales(colname='brand',items=2)
    print(sales)
    context={
        'products':products
    }
    
    return render(request,template,context)