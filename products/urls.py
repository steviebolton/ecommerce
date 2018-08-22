from django.urls import path
from products.views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<id>', product_detail, name='product_detail'),
    ]