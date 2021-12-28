from django.urls import path
from . import views


urlpatterns = [
    path('', views.Leaveapplication.as_view(), name="leave"),
    path('leaveview/<int:id>/', views.LeaveApplicationView.as_view(), name = "ApplyLeaveapplicationview"),
    path('update/<int:pk>/', views.ApplyLeaveUpdateView.as_view(), name="applyleaveupdate"),
    path("leave_reply/",views.LeaveReply.as_view(),name="leave_reply"),
    path('employeeleave/<int:eid>/', views.ViewAllLeave.as_view(), name="employeeleave"),
    path('employeeleaveupdate/<int:pk>/', views.UpdateLeave.as_view(), name="employeeleaveupdate"),
    path('viewcancel_leave/<int:eid>/', views.ViewAllCancelLeave.as_view(), name="viewcancel_leave"),
    path('updatecancel_leave/<int:pk>/', views.UpdateCancelLeave.as_view(), name="updatecancel_leave"),
]
