from cart.forms import CartAddProductForm
from django.shortcuts import render , get_object_or_404 , redirect 
from .models import Product, Category , Like 
from django.db.models import Count
from django.core.paginator import Paginator
from django.utils.text import slugify
import requests
from django.db.models import Q 
from django.urls import resolve
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.files.base import ContentFile
import os
from django.conf import settings
from django.core.mail import send_mail




def index(request , category_slug=None):   
    print(request.get_host())
    categories =  Category.objects.all()
    #this will return all rows with available True and create key total_likes in each product  
    products =  Product.objects.filter(available=True).annotate(total_likes=Count('like'))
    category = None
    #check category_slug if None 
    if category_slug:
        category = get_object_or_404(Category , slug=category_slug)
        query = Q(available=True) & Q(category=category)
        products = Product.objects.filter(query).annotate(total_likes=Count('like'))
    #use paginator 
    paginator = Paginator(products , 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"category":category ,"categories" : categories , "products": page_obj })
    




def product_detail(request, id , slug):
    product = get_object_or_404(Product , id=id , slug=slug)
    #CartAddProductForm() is class to create 
    cart_product_form = CartAddProductForm()
    # on Click delete product if created by user
    if request.method == 'POST' and product.user == request.user :
        product.delete()
        return redirect('index')
    return render(request, "detail.html", {"product":product , 'cart_product_form': cart_product_form })



def products(request):
    products =  Product.objects.filter(available=True).annotate(total_likes=Count('like'))
    paginator = Paginator(products , 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"products": page_obj })


def contact(request):
    return render(request, "contact.html")

def sendEmailToAdmin(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name , 
            message, 
            'settings.EMAIL_HOST_USER',
            [email] , 
            fail_silently=False
        )
        return render(request , 'successful_email_send.html' )
    return render(request , 'contact.html' )

def successful_email_send(request):
    return render(request , 'successful_email_send.html' )


def about(request):
    return render(request, "about.html")







def add_like_product_index(request , id , slug , category_slug=None):
    #get the product 
    product = get_object_or_404(Product, id=id , slug=slug )
    #ckeck if user add like or not if yes delete this from Like models
    if Like.objects.filter(user=request.user, product=product).exists():
        like = Like.objects.filter(user=request.user, product=product).delete()
    else:
        # if not add user and Product to Like models 
        like = Like(user=request.user, product=product)
        like.save()
    if category_slug :
        category = get_object_or_404(Category , slug=category_slug)
        print(category)
        return redirect(category)
    else:
        return redirect('index')
        




def create_data_in_project_from_list(products , user , thumbnail ):
    for product_data in products :
        category_slug = slugify(product_data['category'])
        
        if thumbnail == False:
            image_url = product_data['image']
        else:
            image_url = product_data['thumbnail']

        # Download the image and save it to a temporary file image_response will return <Response [200]>
        image_response = requests.get(image_url)

        temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
        
        
        # ??????????????????????????
        with open(temp_image_path, 'wb') as temp_image_file: 
            temp_image_file.write(image_response.content)

        # Create the category instance if not exist
        category, created = Category.objects.get_or_create(
            slug=category_slug,
            defaults={'name': product_data['category']}
        )
        
        product, _ = Product.objects.get_or_create(
            name=product_data['title'],
            defaults={
                'user': user,
                'slug': slugify(product_data['title']),
                'price': product_data['price'],
                'description': product_data['description'],
                'category': category,
            }
        )
        
        # Save the image file to the product's image field    ????????????????????????
        with open(temp_image_path, 'rb') as image_file:
            product.image.save(f'{product.slug}_image.jpg', image_file)
        
        # Delete the temporary file
        os.remove(temp_image_path)


def add_some_product_from_api_to_database(request):
    try:
        link_api = ["https://fakestoreapi.com/products" , "https://dummyjson.com/products"] 
        for link in link_api:        
            response = requests.get(link)
            response.raise_for_status()  # Raise an exception for any non-successful status codes
            products = response.json()  # Extract JSON data from the response
            if link == "https://fakestoreapi.com/products":
                create_data_in_project_from_list(products , request.user , False)
            elif link == "https://dummyjson.com/products" :
                create_data_in_project_from_list(products['products'] , request.user , True)
        return redirect("index")
    except requests.exceptions.RequestException as e:
        print(f"Error is : {e}")
        return redirect('add_some_product_from_api_to_database')
    
    












from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm 


# we use this function to create Sign Up  
def signup(request):
    # get data from browser if data send by user  if not create fields
    form = SignUpForm(request.POST or None) 
    # if data is valid 
    if form.is_valid():
        # get data valid and save it in variable user  
        user = form.save(commit=False)
        # get cleaned_data password 
        pas = form.cleaned_data.get('password1')
        subject = 'Activate your account' #title Email
        # message to send by email 
        message = 'Please click the link below to activate your account:\n\n' \
                  f'http://localhost:8000/activate/{user.username}/{pas}/{user.email}/'  #link to verify email
        #built-in function in django to send email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
        #if messaege send go to registration_complete.html
        return render(request , 'registration_complete.html')  
    #if form is not valid go to signup to create form 
    return render(request, 'signup.html', {'form': form})


#we use this function to handle activate account when user click link in email 
def activate_account(request, username,password,email):
    try:
        # Create user 
        user = User.objects.create_user(username=username, password=password, email=email)
        # authenticate using email and password
        user = authenticate(username=user.username, password=password)
        # login using user authenticate 
        login(request, user)
    except:
        return redirect('signup')
    # go to page home 
    return redirect('index')  
    