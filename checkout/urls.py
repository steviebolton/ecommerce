from django.urls import path
from .views import view_checkout, confirm_checkout

urlpatterns = [
    path('view/', view_checkout, name='view_checkout'),
    path('confirm/', confirm_checkout, name='confirm_checkout')
    
    ]