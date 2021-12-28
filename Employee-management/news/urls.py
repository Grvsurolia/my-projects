from django.urls import path
from . import views




urlpatterns = [
    path('', views.AllNewsView.as_view(), name="AllNews"),
    path('<int:pk>/', views.NewsView.as_view(), name="News"),
    
    path('newjoinee/', views.NewJoineeAllView.as_view(), name = "AllNewjoinees"),
    path('newjoinee/<int:pk>/', views.NewJoineesView.as_view(), name = "Newjoinees"),
    
    path('birthday/', views.AllBirthdayView.as_view(), name="AllBirthday"),
    path('birthday/<int:pk>/', views.BirthdayView.as_view(), name="Birthday"),
    
    path('holiday/', views.AllUpcomingHolidays.as_view(), name = "AllUpcomingholidays"),
    path('holiday/<int:pk>/', views.UpcomingHolidayView.as_view(), name = "Upcomingholiday"),
    
    path('temprature/',views.Teamprature.as_view()),

]
