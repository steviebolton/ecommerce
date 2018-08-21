

def number_of_items_in_cart(request):

    cart = request.session.get('cart', {})
    return {'number_of_items_in_cart': len(cart)}