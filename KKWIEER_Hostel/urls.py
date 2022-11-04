from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.home, name='name'),
    path('student_dashboard/', views.studentDashboard, name='student_dashboard'),
    path('user/', views.user, name='admin'),
    path('profile/<str:pk_test>/', views.profile, name='profile'),
 
    path('add_student/', views.addStudent, name='add_student'),
    path('update_student/<str:pk>', views.updateStudent, name='update_student'),
    path('delete_student/<str:pk>', views.deleteStudent, name='delete_student'),

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
         name="password_reset_confirm"),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
         name="password_reset_complete"),

]
