from django.urls import path
from .views import create_store , store_list 


urlpatterns = [
    path('create/' , create_store , name="create_store"),
    path('store_list/' , store_list , name="store_list"),
]
