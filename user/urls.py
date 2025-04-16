from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.loginview,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('loginpage/', views.user_login, name='loginuser'),
    path('admindash/',views.admindash,name='adminDash'),
    path('register/',views.register_view,name='register'),
    path('userdash/',views.loginpage,name='loginSuccess'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),

    # Password reset URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
