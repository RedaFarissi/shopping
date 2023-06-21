from django.shortcuts import render , redirect 
from .forms import StoreForm , ProductForm
from .models import Store 
from shop.models import Product
from django.utils.text import slugify

def create_store(request):
    #check if user authenticated
    if request.user.id is None: 
        return redirect('index')
    try:
        #check if user have store  
        store = Store.objects.get(user=request.user.id)
        return redirect('store_list')
    except:
        #create Store if not exist
        form = StoreForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            store = form.save(commit=False)
            store.user = request.user
            store.slug = slugify(store.name)
            store.save()
            return redirect('store_list')
    return render( request , 'create_store.html' , {'form':form} )



def store_list(request):
    #check if user authenticated
    if request.user.id is None: 
        return redirect('index')
    
    products = Product.objects.filter(user=request.user)
    store = Store.objects.get(user=request.user)
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.slug = slugify(product.name)          
        product.save()
        return redirect('index')
    return render(request , 'store_list.html' , {'store_products':products , 'store_name':store.name , 'form':form})