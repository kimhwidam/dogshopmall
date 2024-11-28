from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_from_cart

urlpatterns = [
    path('cart_items/', views.cart_items, name='cart_items'),

    # path('<str:product_id>/<int:user/', views.add_to_cart, name='add_to_cart'),

    path('delete_from_cart/<int:cart_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('<str:product_id>/<int:user>/', views.add_to_cart, name='add_to_cart'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)