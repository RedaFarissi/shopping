from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')) ,
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('create_store/', include("create_store.urls")) ,
    # path('paypal/', include("paypal.standard.ipn.urls")),
    path('payments/', include("payments.urls")),
    path('s/', include("scraping.urls")) ,
    path('', include("shop.urls")) ,
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)