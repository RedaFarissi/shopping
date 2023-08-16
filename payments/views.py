import uuid
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from orders.models import Order

def process_payment(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    
    host = request.get_host()
    
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.get_total_cost() ,
        'item_name': order.id,
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}' ,
        'return_url': f'http://{host}{reverse("payment_done")}',
        'cancel_return': f'http://{host}{reverse("payment_cancelled")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process_payment.html', {'form': form , 'order':order})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')