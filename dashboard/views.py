from django.shortcuts import render
from .models import *




def home(request):
    template='dashboard/home.html'
    category_sales=Product.category_sales(get='Highest')
    stats=Product.inventory_overview()
    categories = [item['category'] for item in category_sales]
    sales = [float(item['total_sales']) for item in category_sales]
    print(stats)
    context={
        'categories':categories,
        'sales':sales,
        'stats':stats,
    }

    return render(request,template,context)