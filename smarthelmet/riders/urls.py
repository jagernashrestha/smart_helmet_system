from django.urls import path
from . import views

urlpatterns = [
    path('', views.rider_list, name='rider_list'),
    path('add/', views.rider_add, name='rider_add'),
    path('edit/<int:pk>/', views.rider_edit, name='rider_edit'),
    path('delete/<int:pk>/', views.rider_delete, name='rider_delete'),
]
