from django.shortcuts import render
from .models import *
from .serializers import ProductSerializer
from rest_framework import viewsets


def home(request):
    template='dashboard/home.html'
    
    category_sales=Product.category_sales(get='Highest')
    stats=Product.inventory_overview()
    categories = [item['category'] for item in category_sales]
    sales = [float(item['total_sales']) for item in category_sales]

    print(category_sales)
    
    context={
        'categories':categories,
        'sales':sales,
        'stats':stats,
    }

    return render(request,template,context)


def inventory(request):
    template='dashboard/inventory.html'
    context={
        
    }
    return render(request,template,context)

class InventoryView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_options(self):
        return "options", {
            "product_name": [{'label': obj.product_name, 'value': obj.pk} for obj in Product.objects.all()],
        }
    
    class Meta:
        datatables_extra_json = ('get_options',)

   
    