from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
    # start
    path('', views.start, name='start'),
    path('ToBeTogether/', views.ToBeTogether, name='ToBeTogether'),
    # account
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('my_issues/', views.my_issues, name='my_issues'),
    # change password
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # edit profile
    path('settings/', views.settings, name='settings'),
    path('edit/', views.edit, name='edit'),
]
