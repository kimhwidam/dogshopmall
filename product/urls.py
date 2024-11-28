from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product_view/', views.product_view, name='product_view'),
    path('product_view/<str:brand_code>/', views.product_view, name='product_view_brand'),
    path('<str:product_id>/', views.product_detail, name='product_detail'),
    path('<str:product_id>/submit_review/', views.submit_review, name='submit_review'),
]

