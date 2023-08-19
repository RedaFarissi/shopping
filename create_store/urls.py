from django.urls import path
from .views import   store_list 

urlpatterns = [
    path('store_list/' , store_list , name="store_list"),
]
