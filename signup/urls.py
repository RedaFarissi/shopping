from django.urls import path
from . import views

# app_name = 'signup'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('activate/<str:username>/<str:password>/<str:email>/', views.activate_account, name='signup_activate'),   
]