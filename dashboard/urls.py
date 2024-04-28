
from django.urls import path ,include, re_path
from dashboard import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'inventory', views.InventoryView)


urlpatterns = [
    path('home/',views.home,name='home'),
    path('inventory/',views.inventory,name='inventory'),
     re_path('^api/', include(router.urls))
]
