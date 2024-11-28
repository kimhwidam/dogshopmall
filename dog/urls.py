from django.urls import path
from . import views 

urlpatterns = [
    path('recommendation/', views.recommendation_view, name='recommendation'),
    path('recommendation_results/', views.recommendation_results, name='recommendation_results'),
]
