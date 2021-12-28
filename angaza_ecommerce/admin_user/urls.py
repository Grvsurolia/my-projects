from django.urls import path, include
from .views import *
from users import views

urlpatterns = [

    path("add_size/", AddSize.as_view(), name="add_size"),
    path('update_size/<int:pk>/', SizeUpdate.as_view(), name="update_size"),
    path("add_color/", AddColours.as_view(), name="add_color"),
    path('update_color/<int:pk>/', ColoursUpdate.as_view(), name="update_color"),
    path("add_brand/", AddBrands.as_view(), name="add_brand"),
#     path("add_subproduct/",AddSubproduct.as_view(),name="add_subproduct"),
#     path("update_subproduct/",SubProductUpdate.as_view(),name="update_subproduct"),



    path('update_brand/<int:pk>/', BrandUpdate.as_view(), name="update_brand"),
    path('add_homepage_adv/', AddHomePagesAdvertisement.as_view(),
         name="add-homepage-adv"),
    path('update_home_adv/<int:pk>/',
         HomePagesAdvertisementUpdate.as_view(), name="update-home-adv"),

    path("add_detailpage_adv/", AddDeatilPagesAdvertisement.as_view(),
         name="add-detailpage-adv"),
    path('update_details_adv/<int:pk>/',
         DeatilPagesAdvertisementUpdate.as_view(), name="update-detail-adv"),

    path("all_home_adv/", ViewAllHomePagesAdvertisement.as_view(), name="all-home-adv"),

    path('numberwise_detail_adv/',
         ViewNumberWiseDetailPagesAdvertisement.as_view(), name="numberwise-detail-adv"),
    path('connect_productwith_deal/', ProductConnectWithDeal.as_view(),
         name='connect-productwith-deal'),


]
