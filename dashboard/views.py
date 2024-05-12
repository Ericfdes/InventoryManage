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

    recent_sales=Sale.objects.order_by('-date_sold')[:6]
    print(recent_sales)
  
    
    context={
        'categories':categories,
        
        #bar
        'sales':sales,
        'stats':stats,
        
        #line
        'line_sales':line_sales,
        'line_month':line_month,

        #latest sales
        'recent_sales':recent_sales
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

def compare(request):
    col_name =  chart = sales = None
    if request.GET:
        column = request.GET.get('col')
        ranges = request.GET.get('range')
        chart = request.GET.get('chart')
        compare_sales=Product.total_sales(colname=column,get=ranges)
        print(compare_sales)
        col_name = [item[column] for item in compare_sales]
        sales = [float(item['total_sales']) for item in compare_sales]

        print(col_name)
        print(sales)


    template='dashboard/compare.html'

   



    
    context={

        'col_name' : col_name,
        'sales' : sales,
        'chart' : str(chart)
        

    }




    return render(request,template,context)

   
    