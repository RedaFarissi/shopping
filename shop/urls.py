from django.urls import path
from . import views

# app_name = 'app'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api_product/', views.add_some_product_from_api_to_database , name='add_some_product_from_api_to_database'),
    path('products/', views.products , name='products'),
    path('contact/', views.contact , name='contact'),
    path('send_email/' , views.sendEmailToAdmin , name="send_email" ),
    path('about/', views.about , name='about'),

    path('successful_email_send/' , views.successful_email_send , name="successful_email_send" ),
    path('activate/<str:username>/<str:password>/<str:email>/', views.activate_account, name='signup_activate'),   
    path('add_like/<int:id>/<slug:slug>/', views.add_like_product_index , name='add_like_product'),
    path('add_like/<int:id>/<slug:slug>/<slug:category_slug>/', views.add_like_product_index , name='add_like_product_category'),
    path("<int:id>/<slug:slug>/", views.product_detail , name="product_detail"),
    
    
    path("" , views.index  , name="index"),
    path("<slug:category_slug>/" , views.index  , name="product_list_by_category"),

]