from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('agregar/', views.add_post, name='add_post'),
    path('aleatorio/', views.random_post, name='random_post'),
    path('buscar/', views.search, name='search'),
    path('eliminar/<int:pk>/', views.delete_post, name='delete_post'),
]
