from django.urls import path 
from . import views


urlpatterns = [
    path('', views.contact , name='contact'),
    path('send_email/' , views.sendEmailToAdmin , name="send_email" ),
    path('successful_email_send/' , views.successful_email_send , name="successful_email_send" ),
]
