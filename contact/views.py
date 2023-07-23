from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    return render(request, "contact.html")


def sendEmailToAdmin(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name , #title
            message, #message
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        return render(request , 'successful_email_send.html' )
    return render(request , 'contact.html' )


def successful_email_send(request):
    return render(request , 'successful_email_send.html' )
