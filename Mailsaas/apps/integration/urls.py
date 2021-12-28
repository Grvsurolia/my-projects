from django.urls import path

from . import views

# from .routers import router


urlpatterns = [
    path('sforce/', views.ContactViewSet.as_view()),
    path("sforce/add/", views.SalesForceDetailStore.as_view()),
    path("sforce/edit/<int:pk>/", views.SalesForceDetailUpdate.as_view()),
    path('event/hook/', views.event_hook, name='event_hook')

]
