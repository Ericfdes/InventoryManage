from django.db import models
from django.db.models import Sum, Max, Count ,F
import random

def gen_inventory():
    return random.randint(10,100)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    absolute_url = models.URLField()
    sold = models.IntegerField()
    temperature = models.CharField(max_length=10)
    quantity_value = models.FloatField(null=True)
    quantity_type = models.CharField(max_length=50, null=True)
    #inventory=models.IntegerField(default=gen_inventory())
    
    
    @classmethod
    def inventory_overview(cls):
        total_products = cls.objects.count()
        total_quantity_in_stock = cls.objects.aggregate(total_quantity=Sum('quantity_value'))['total_quantity']
        total_sales = cls.objects.aggregate(total_sales=Sum('sold'))['total_sales']
        
        sales=models.F('price') * models.F('sold')
        discount=models.F('discount_price') * models.F('sold')
        total_revenue_generated = cls.objects.annotate(
            revenue=models.ExpressionWrapper(
                sales - discount,
                output_field=models.DecimalField()
            )
        ).aggregate(total_revenue=Sum('revenue'))['total_revenue']
        total_revenue_generated=float(total_revenue_generated)/10000000#convert  to crore
        total_revenue_generated=round(total_revenue_generated,2)
        total_quantity_in_stock=int(total_quantity_in_stock)
        return {
            'total_products': total_products,
            'total_quantity_in_stock': total_quantity_in_stock,
            'total_sales': total_sales,
            'total_revenue_generated': total_revenue_generated
        } 
        
    @classmethod    
    def category_sales(cls,get):
        category_sales = cls.objects.values('category').annotate(total_sales=Sum('price')*F('sold'))

     
        unique_categories = {}
        for entry in category_sales:
            category = entry['category']
            total_sales = entry['total_sales']

           
            if category in unique_categories:
           
                unique_categories[category] += total_sales
            else:
              
                unique_categories[category] = total_sales

        result = [{'category': category, 'total_sales': total_sales} for category, total_sales in unique_categories.items()]

        # Sort the result by total sales in descending order
        result.sort(key=lambda x: x['total_sales'], reverse=True)

        if get == 'Highest':
            return result[:5]
        elif get == 'Least':
            return result[-5:]
        else:
            return None

        
    @classmethod
    def total_sales(cls,items,colname=None,colist=None,):
        
        if items is not None:
            total_items=items
        else:
            total_items=3
            
        if colname is not None:
            filter_row = {f'{colname}__exact': 'nan'}  
            sales = cls.objects.exclude(**filter_row).values(colname).annotate(total_sales=Count('sold'))
            #sales = cls.objects.values(colname).annotate(total_sales=Count('sold'))
            if sales.exists():
                    highest_sales = sales.order_by('-total_sales')[:total_items]
                    least_sales= sales.order_by('-total_sales')[total_items:]
                    return {
                        f'highest_sales_{colname}':highest_sales,
                        f'least_sales_{colname}':least_sales
                    }
            else:
                return None
                
        elif colist is not None:
            if not isinstance(colist, list):
                raise TypeError("Cols should be given in a list")
            result = {}
            for col in colist:
                filter_row = {f'{colname}__exact': 'nan'} 
                sales = cls.objects.values(col).annotate(total_sales=Count('sold')).exclude(**filter_row)
                if sales.exists():
                    highest_sales = sales.order_by('-total_sales')[:total_items]
                    least_sales = sales.order_by('-total_sales')[total_items:]
                    result[f'highest_sales_{col}'] = highest_sales
                    result[f'least_sales_{col}'] = least_sales
                else:
                    result[f'highest_sales_{col}'] = None
                    result[f'least_sales_{col}'] = None
            return result
        
        else:
            return 'args missing'
   

    def __str__(self):
        return self.product_name
    