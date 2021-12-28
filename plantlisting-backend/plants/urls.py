from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
   path('filter/',views.FilterPlant.as_view(), name = 'plant-post'),   
   path('userplants/',views.GetPlantsByUser.as_view(),  name="UserPlants"),
   path('plantpost/',views.Plants.as_view(),  name="Plants"),
   path('updateplant/<int:pk>/',views.PlantDetailView.as_view(),  name="PlantDetailUpdate"),
   path('usercontactview/<int:pk>/',views.Usercontactapi.as_view(),name = 'usercontactview'),
   path('plant-type/',views.PlantTypeView.as_view(), name="PlantTypePost"),
   path('plant-type/<int:pk>/', views.PlantTypeDetailView.as_view(), name="UpdateP_Type"),
   path('wishlist/',views.Wishlist.as_view(), name = "wishlist"),
   path('wishlistview/',views.WishListView.as_view(), name = "wishlistview"),
   path('wishlistview/<int:pk>/',views.WishListDeleteView.as_view(), name = "wishlistDelete"),
   path('plant-view/',views.ProductList.as_view()),
   path('plant-types/',views.PlantTypeView.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)