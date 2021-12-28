from django.urls import path
from . import views




urlpatterns = [
    path('', views.DocumentationView.as_view(), name="documentation"),
    path('policy/', views.Policyview.as_view(), name="policy"),
    path('form/', views.Formview.as_view(), name="form"),
    path('<int:pk>/', views.DocumentationUpdateView.as_view(), name="updatedelete"),

]