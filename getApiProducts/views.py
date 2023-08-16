from django.shortcuts import redirect
from shop.models import Product, Category , Color , Size
from .product_api import  products_api 
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
import os

@login_required
def add_some_product_from_api_to_database(request):    
    for product_data in products_api :    
        # Create the category instance if not exist
        category, _ = Category.objects.get_or_create(
            slug=slugify(product_data['category']),
            defaults={'name': product_data['category']}
        )   

        #create instence from Category used
        check_category = Category.objects.get(name=product_data['category'])
       
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            user=request.user,
            defaults={
                'category': check_category,
                'slug': slugify(product_data['name']),
                'description': product_data['description'],
                'price': product_data['price'],
            }
        )

        # If the product was created, load and save the image
        if created:
            image_path = os.path.join('static/products_test_img', product_data['image'])
            with open(image_path, 'rb') as image_file:
                product.image.save(product_data['image'], ContentFile(image_file.read()), save=True)

    

        
        # Retrieve Size instances based on size names
        size_names = product_data['sizes']
        sizes = Size.objects.filter(name__in=size_names)
        product.sizes.set(sizes)

    return redirect('index')
        