from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')) ,
    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('create_store/', include("create_store.urls")) ,
    path('contact/', include("contact.urls")) ,
    path('signup/', include("signup.urls")) ,
    path('products_api/', include("getApiProducts.urls")) ,
   
    path('payments/', include("payments.urls")),
    path('s/', include("scraping.urls")) ,
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include("shop.urls")) ,
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)