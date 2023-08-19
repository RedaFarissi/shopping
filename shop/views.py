from cart.forms import CartAddProductForm
from django.shortcuts import render , get_object_or_404 , redirect 
from .models import Product, Category , Like 
from django.db.models import Count
from django.core.paginator import Paginator
from django.db.models import Q 
from django.contrib.auth.decorators import login_required

def index(request , category_slug=None):   
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
    products =  Product.objects.filter(available=True)
    paginator = Paginator(products , 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"products": page_obj })


def about(request):
    return render(request, "about.html")

@login_required
def add_like_product_index(request , id , slug , category_slug=None):
    #get the product 
    product = get_object_or_404( Product, id=id , slug=slug )

    
    if Like.objects.filter(user=request.user, product=product).exists():
        like = Like.objects.filter(user=request.user, product=product).delete()
    else:
        # if not add user and Product to Like models 
        like = Like(user=request.user, product=product)
        like.save()
    
    if category_slug :
        category = get_object_or_404(Category , slug=category_slug) 
        return redirect('product_list_by_category', category_slug=category_slug)    
    return redirect('index')