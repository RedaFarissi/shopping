from django.urls import path
from .views import index , product_detail , add_like_product_index , signup , activate_account , add_some_product_from_api_to_database 

# app_name = 'app'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('api_product/', add_some_product_from_api_to_database , name='add_some_product_from_api_to_database'),
    path('activate/<str:username>/<str:password>/<str:email>/', activate_account, name='signup_activate'),   
    path('add_like/<int:id>/<slug:slug>/', add_like_product_index , name='add_like_product'),
    path('add_like/<int:id>/<slug:slug>/<slug:category_slug>/', add_like_product_index , name='add_like_product_category'),
    path("<int:id>/<slug:slug>/", product_detail , name="product_detail"),
    
    path("" , index  , name="index"),
    path("<slug:category_slug>/" , index  , name="product_list_by_category"),

]