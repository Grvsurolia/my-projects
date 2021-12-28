from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateTeamView.as_view(), name="teams"),
    path('change/<int:pk>/', views.UpdateDeleteTeams.as_view(), name="change"),
    path('invite/', views.SendTeamInvitionsView.as_view(), name="invite"),
    path('register/<slug:id>',views.RegisterTeamMember.as_view(),name='member')
    
]