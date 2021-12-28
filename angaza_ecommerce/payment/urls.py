from django.urls import path
from django.contrib.auth import views
from .import views

urlpatterns = [
    path('send_payment_request/', views.SendPaymentRequest.as_view(), name="send_payment_request"),
    path('check_payment/', views.CheckPayment.as_view(), name="check_payment"),
    # path('payment/', views.getAccessToken, name="payment"),

]
