from django.shortcuts import render , redirect
from shop.models import Product, Category
from django.urls import resolve
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.files.base import ContentFile
import os
from django.conf import settings
import requests
from django.utils.text import slugify

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
