from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import OrderLineItem

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
    
    return render(request, "checkout/view_checkout.html", {'form': form})