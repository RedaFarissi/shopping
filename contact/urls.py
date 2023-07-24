from django.urls import path 
from . import views


urlpatterns = [
    path('', views.contact , name='contact'),
    path('send_email/' , views.sendEmailToAdmin , name="send_email" ),
    path('successful_email_send/' , views.successfulEmailSend , name="successful_email_send" ),
    path('all_message_from_user/' , views.allMessageFromUser , name="all_message_from_user" ),
    path('reply_to_the_user/<str:email>/<int:pk>' , views.replyToTheUser , name="reply_to_the_user" ),
]
