from django.shortcuts import render , redirect 
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm

from cryptography.fernet import Fernet




key_encrypt = "QredasPn3"

def encrypt_string(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_string(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message







# we use this function to create Sign Up  
def signup(request):
    # get data from browser if data send by user  if not create fields
    form = SignUpForm(request.POST or None) 
    # if data is valid 
    if form.is_valid():
        # get data valid and save it in variable user  
        user = form.save(commit=False)
        pas = form.cleaned_data.get('password1')
        title = 'Activate your account' #title Email
        message = 'Please click the link below to activate your account:\n\n ' \
                  f'http://localhost:8000/signup/activate/{user.username}/{pas}/{user.email}/' 
        send_mail(title, message, settings.EMAIL_HOST_USER, [user.email])
        return render(request , 'registration_complete.html')  
    return render(request, 'signup.html', {'form': form})


def activate_account(request, username,password,email):
    try:
        #Create user 
        user = User.objects.create_user(username=username, password=password, email=email)

        # authenticate using email and password
        user = authenticate(username=user.username, password=password)
        # login using user authenticate 
        login(request, user)
    except:
        return redirect('signup')
    # go to page home 
    return redirect('index')  
    
