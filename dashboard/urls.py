
from django.urls import path ,include, re_path
#http://localhost:8000/api/inventory/?
from dashboard import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'inventory', views.InventoryView)
router.register(r'sale', views.SaleView)


urlpatterns = [
    path('home/',views.home,name='home'),
    path('inventory/',views.inventory,name='inventory'),
    path('sale/',views.sale,name='sale'),
    re_path('^api/', include(router.urls))
]
