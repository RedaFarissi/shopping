from django.urls import reverse
from django.shortcuts import render , redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

         # add class to html
        for _ , field in form.fields.items():
            field.widget.attrs['class'] = 'form-control order-form-input'

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'] ,price=item['price'], quantity=item['quantity'])
            cart.clear()
            
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('process_payment'))
        
    else:
        form = OrderCreateForm()
    return render(request , 'create.html', {'cart': cart, 'form': form})