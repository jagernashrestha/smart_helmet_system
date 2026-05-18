from django.urls import path
from . import views

urlpatterns = [
    path('', views.accident_list, name='accident_list'),
    path('<int:pk>/', views.accident_detail, name='accident_detail'),
    path('<int:pk>/resolve/', views.accident_resolve, name='accident_resolve'),
    path('helmets/', views.helmet_status, name='helmet_status'),
]
