from django.shortcuts import render
from .models import *
from .serializers import ProductSerializer,SaleSerializer
from rest_framework import viewsets


def home(request):
    template='dashboard/home.html'
    
    category_sales=Product.category_sales(get='Highest')
    stats=Product.inventory_overview()
    month_sales=Sale.get_monthwise_sales()
    #bar
    categories = [item['category'] for item in category_sales]
    sales = [float(item['total_sales']) for item in category_sales]
    
    #line
    line_month=[item['month'] for item in month_sales]
    line_sales=[item['total_sales'] for item in month_sales]
    monthwise=Sale.get_monthwise_sales()
    print(monthwise)
    
    context={
        'categories':categories,
        
        #bar
        'sales':sales,
        'stats':stats,
        
        #line
        'line_sales':line_sales,
        'line_month':line_month,
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

def sale(request):
    template='dashboard/Sale.html'
    context={
        
    }
    return render(request,template,context)

class SaleView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    
    # def get_options(self):
    #     return "options", {
    #         "product_name": [{'label': obj.product_name, 'value': obj.pk} for obj in Product.objects.all()],
    #     }
    
    # class Meta:
    #     datatables_extra_json = ('get_options',)

   
    