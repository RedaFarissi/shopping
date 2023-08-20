from django.shortcuts import render , redirect 
from .forms import  ProductForm 
from shop.models import Product
from django.utils.text import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def store_list(request):
    products = Product.objects.filter(user=request.user).annotate(total_likes=Count('like')).order_by('-id') 
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.slug = slugify(product.name)          
        product.save()
        return redirect('store_list')
    return render(request , 'store_list.html' , {'products_created_by_user':products , 'form':form})