from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="auth-register"),
    path('login/', views.LoginView.as_view(), name="auth-login"),
    path('reset_password/', views.GenerateToken.as_view(), name="reset_password"),
    path('token/<str:token_data>/',views.ResetPassword.as_view(),name="token_password"),
    path('update_password/', views.ChangePasswordView.as_view(), name ="update_password"),
    path('profile_update/<int:pk>/', views.UserProfileUpdateView.as_view(), name ="user_update"),
]

