from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product


# Create your views here.
def view_checkout(request):
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            cart = request.session.get('cart', {})
            
            for product, quantity in cart.items():
                line_item = OrderLineItem(
                    order=order,
                    product_id = product,
                    quantity = quantity
                    )
                line_item.save()
                
            del request.session['cart']
            
            return redirect("home")
    else:
        form = OrderForm()
    
    
    cart = request.session.get('cart', {})

    total = 0
    cart_items = []
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'total': item_total})


    return render(request, "checkout/view_checkout.html", {'form': form, 'cart_items': cart_items, 'total': total})