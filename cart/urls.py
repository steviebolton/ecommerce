from django.urls import path
from .views import view_cart, add_to_cart, remove_item

urlpatterns = [
    path('view/', view_cart, name="view_cart"),
    path('add/', add_to_cart, name="add_to_cart"),
    path('remove/', remove_item, name="remove_item")
]

