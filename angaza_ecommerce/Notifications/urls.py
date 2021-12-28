from django.contrib.auth import views
from django.urls import path

from . import views

urlpatterns = [
    path('view_notification/', views.ViewAllNotification.as_view(), name="view-notification"),
    path('delete_notification/<int:pk>/', views.DeleteNotification.as_view(), name="delete-notification"),
]
