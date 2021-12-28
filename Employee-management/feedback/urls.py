from . import views
from django.urls import path

urlpatterns = [
    path('', views.AddFeedBack.as_view(), name="add_feedback"),
    path('update/<int:pk>/', views.UpdateFeedBack.as_view(), name = "update_feedback"),
    path('view_feedback/', views.ViewFeedback.as_view(), name = "view_feedback"),
  
]
