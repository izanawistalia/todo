from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('index/', views.index, name='index'),
    path('add/', views.add, name='add'),
    #path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
