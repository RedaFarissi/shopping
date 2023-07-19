from django.shortcuts import render

from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

    

def view_that_asks_for_money(request):
    paypal_dict = {
        "business": "redaredaeskouni@gmail.com",
        "amount": "1.00",
        "item_name": "name of the item",
        "invoice": "EMe7LGGXl1PUMYL7SUnlX8Mq4poVpaorCZX6ypxi9ZBEPp0bgF0m23Jox9iMcNvggjh4kXRQFG1A6327",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('successful')),
        "cancel_return": request.build_absolute_uri(reverse('concelled')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

def concelled(request):
    return render(request, "concelled.html")

def successful(request):
    return render(request, "successful.html")
