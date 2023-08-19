from django.urls import path
from . import views

# app_name = 'shop'

urlpatterns = [
    
    #path('api_product/', views.add_some_product_from_api_to_database , name='add_some_product_from_api_to_database'),
    path('products/', views.products , name='products'),
    path('about/', views.about , name='about'),
   
    path('add_like/<int:id>/<slug:slug>/', views.add_like_product_index , name='add_like_product'),
    path('add_like/<int:id>/<slug:slug>/<slug:category_slug>/', views.add_like_product_index , name='add_like_product_category'),
    
    path("" , views.index  , name="index"),
    path("<slug:category_slug>/" , views.index  , name="product_list_by_category"),
    path("<int:id>/<slug:slug>/", views.product_detail , name="product_detail"),

]