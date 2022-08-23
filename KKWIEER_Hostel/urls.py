from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='name'),
    path('user/', views.user, name='admin'),
    path('profile/<str:pk_test>/', views.profile, name='profile'),

    path('add_student/', views.addStudent, name='add_student'),
    path('update_student/<str:pk>', views.updateStudent, name='update_student'),
    path('delete_student/<str:pk>', views.deleteStudent, name='delete_student'),

]
