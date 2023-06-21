from .cart import Cart

# this function is used like context processors we add it in templates list in settings to can get cart from any file in templates.
def cart(request):
    return {'cart': Cart(request)}