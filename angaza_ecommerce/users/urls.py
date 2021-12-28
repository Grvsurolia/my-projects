from django.urls import include, path

from users import views

from .views import *

urlpatterns = [

    path('register/', RegisterCustomersView.as_view(), name="register"),
    path('verify_email/', verifyEmailOtp.as_view(), name="verify_email"),
    path('login/', LoginUserView.as_view(), name="login"),
#     path('token_verify/', IsTokenValid, name="token-verify"),
# 
    path('reset_password/', views.GenerateToken.as_view(), name="reset_password"),
    path('token/', views.ResetPassword.as_view(), name="token_password"),
    path('update_password/', views.ChangePasswordView.as_view(),
         name="update_password"),
    path('profile_update/<int:pk>/',
         views.UserProfileUpdateView.as_view(), name="user_update"),
    path('subscribe/', AddSubscribe.as_view(), name="subscribe"),
    path('add_address/', AddressAdd.as_view(), name="add-address"),
    path('address_view/<int:uid>/',
         views.GetCustomerAddress.as_view(), name="address-update"),
    path('address_update/<int:pk>/',
         views.AddressUpdateView.as_view(), name="address-update"),
    path("contact/",views.CreateContactForm.as_view(),name="add-contact"),
]
