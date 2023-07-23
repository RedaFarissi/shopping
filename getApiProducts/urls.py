from django.urls import path
from . import views

# app_name = 'shop'

urlpatterns = [
    
    path('api_product/', views.add_some_product_from_api_to_database , name='add_some_product_from_api_to_database'),

]