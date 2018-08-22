
def number_of_items_in_cart(request):
    cart = request.session.get('cart', {})
    count = sum(cart.values())
    return { 'number_of_items_in_cart': count }
