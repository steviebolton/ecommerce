from django.urls import path
from .views import view_checkout

urlpatterns = [
    path('view/', view_checkout, name="view_checkout")
    ]