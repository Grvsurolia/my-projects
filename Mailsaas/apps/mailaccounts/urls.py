from django.urls import path

from . import views

urlpatterns = [
    path('addmailaccount/', views.EmailAccountsView.as_view(), name="addmailaccount"),
    path('updatedeletemailaccount/<int:pk>/',views.EmailAccountsUpdateView.as_view(), name = 'updatedeletemailaccount'),
    path('googleaccountadd/',views.GoogleAccountsAddView.as_view(), name = 'googleaccountadd'),
    path('testget/',views.TestGetView.as_view(), name = 'TestGetView'),
]
