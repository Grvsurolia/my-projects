from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.LoginView.as_view(), name="auth-login"),
    path('register/', views.RegisterView.as_view(), name="auth-register"),
    path('reset_password/', views.GenerateToken.as_view(), name="reset_password"),
    path('token/<str:token_data>/',views.ResetPassword.as_view()),
    path('add_department/', views.AddDepartment.as_view(), name="add_department"),
    path('update_department/<int:pk>/', views.DepartmentUpdate.as_view(), name="update_department"),
    path('delete_department/<int:pk>/', views.DepartmentDelete.as_view(), name="delete_department"),
    path('update_password/', views.ChangePasswordView.as_view(), name ="update_password"),
    path('allemployee/', views.ViewAllEmployee.as_view(), name ="allemployee"),
    path('profile_update/<int:pk>/', views.UserProfileUpdateView.as_view(), name ="user_update"),
    path('employee_ownprofile_update/<int:pk>/', views.UserOwnProfileUpdate.as_view(), name ="employee_ownprofile_update"),
    path('update_request/', views.RequestFromView.as_view(), name ="update_request"),
    path('viewupdaterequest/<int:pk>/', views.ViewRequestFrom.as_view(), name ="viewupdaterequest"),
    path('profile_delete/<int:pk>/', views.UserProfileDelete.as_view(), name ="user_date"),
    path('bank_account/', views.BankDetails.as_view(), name ="BankAdd"),
    path('bankdetail_view/<int:pk>/', views.Bankdetailsview.as_view(), name ="bankdetail_view"),
    path('bankdetail_delete/<int:pk>/', views.BankDetailDelete.as_view(), name ="bankdetail_delete"),
]