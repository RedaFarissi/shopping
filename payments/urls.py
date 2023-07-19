from django.urls import path , include
from . import views
urlpatterns = [
    path("successful/", views.successful , name="successful" ),
    path("concelled/", views.concelled , name="concelled" ),
    path("", views.view_that_asks_for_money , name="view_that_asks_for_money "),

    path('paypal/', include("paypal.standard.ipn.urls")),
]
