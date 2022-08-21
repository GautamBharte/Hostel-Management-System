from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='name'),
    path('user/', views.user, name='admin'),
    path('profile/<str:pk_test>/', views.profile, name='profile'),
]
