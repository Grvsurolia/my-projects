from django.urls import path, include
from CustomUserModel.views import *
from CustomUserModel import views



urlpatterns = [
    
    path('register/', RegisterUsersView.as_view(), name="auth-register"),
    path('activate/<uidb64>/<token>/',VerificationView.as_view(), name='activate'),
    path('account-activation/',AccountActivation.as_view(), name = 'account-activate'),
    path('login/', Login.as_view(), name="auth-login"),
    path('google/', views.GoogleView.as_view(), name='google'),
    path('updatepassword/', UpdatePassword.as_view(), name="password_update"),
    path('users/', GetAllUserByAdmin.as_view(), name = 'Get_Users'),
    path('profile/', UserProfileUpdateView.as_view(), name="UpdateProfile"),
    path("otp-login/", LoginWithOtp.as_view(), name="OTP_Gen"),
    path('forgot-password/', Generate_token.as_view(),name="OTP_Gen"),
    path('token/<str:token_data>/',UserForgetPassword.as_view(),name="forgot_password"),
    path('facebook/', SocialLoginView.as_view(),name="facebook_login"),
    path('subscribe/',EmailSubscription.as_view(),name="subscribe"),
    path('message/',MessagePost.as_view(),name="message"),
    path('message-get/',MessageGet.as_view(),name='message-get'), # for temp purpose
    path('is_verify/',CheckVerification.as_view(),name="check_verification")
    
]