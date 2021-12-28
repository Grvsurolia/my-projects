from django.urls import path
from . import views


pp_name = 'unsubscribes'
urlpatterns = [
    path('',views.UnsubscribeEmailAdd.as_view(), name ='unscribe'),
    path('unsubcribecsv/',views.UnsubcribeCsvEmailAdd.as_view(), name ='unsubcribecsv'),
    path('unsubcribeview/',views.UnsubcribeEmailView.as_view(), name ='unsubcribeview'),
    path('unsubcribedelete/',views.UnsubcribeEmailDelete.as_view(), name ='unsubcribedelete'),
]
