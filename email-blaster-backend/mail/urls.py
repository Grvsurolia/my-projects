from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from mail import views

urlpatterns = [
    path('account/', views.AddMailAccount.as_view()),
    path('account/<int:pk>/', views.MailAccountDetail.as_view()),
    path('email/', views.AddEmailView.as_view()),
    path('email/open/<slug:id>', views.TrackEmailOpen.as_view(), name='track_email_open'),
    path('email/click/<str:id>', views.TrackEmailClick.as_view(), name='track_email_click'),




]
