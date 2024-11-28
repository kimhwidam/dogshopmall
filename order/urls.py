# order/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('order_list/', views.order_list, name='order_list'),
    # 다른 URL 패턴들을 여기에 추가할 수 있습니다.
    path('order_create/', views.order_create, name='order_create'),  # 추가

]

