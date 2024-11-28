from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'user'

urlpatterns = [
    path('registration/', views.register, name='registration'),  # 'register' 뷰를 사용하도록 지정
    path('login/', LoginView.as_view(template_name='user/login_view.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]

