from django.shortcuts import render , redirect , get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUser
from .forms import ContactForm

def contact(request):
    return render(request, "contact.html")


def sendEmailToAdmin(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']
        contact_user = ContactUser.objects.create(
            email=email, subject=subject, message=message
        )
        contact_user.save()
        return redirect('successful_email_send')
    return render(request , 'contact.html' )


def successfulEmailSend(request):
    return render(request , 'successful_email_send.html' )

def allMessageFromUser(request):
    contact_users = ContactUser.objects.order_by('-contact_date') 
    return render(request , 'all_message_from_user.html' , {'contact_users': contact_users})


def replyToTheUser(request, email , pk ):
    message = request.POST['message']
    subject = request.POST['subject']
    send_mail(subject , message, settings.EMAIL_HOST_USER, [email])
    contact = get_object_or_404(ContactUser, pk=pk , email=email)
    contact.vu = True
    contact.save()
    return redirect('all_message_from_user')