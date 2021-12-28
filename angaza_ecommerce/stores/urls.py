from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('add_store/', views.AddStore.as_view(), name="add-store"),
    path("update_store/<int:pk>/", views.StoreUpdate.as_view(), name="update-store"),
    path('add_product/', views.AddProducts.as_view(), name="add-product"),
    path('update_product_details/<int:pk>/',views.ProductUpdate.as_view(), name="view_product_details"),
    path('add_description/', views.AddProductDescription.as_view(),
         name="add-description"),
    path('update_product_description/<int:pk>/',
         views.UpdateProductDescription.as_view(), name="view_product_details"),
    path('add_product_size/', views.AddProductSize.as_view(),
         name="add-product-size"),
    path("update_product_size/<int:pk>/",
         views.UpdateProductSize.as_view(), name="update-product-size"),

    path('add_product_color/', views.AddProductColour.as_view(),
         name="add-product-color"),
    path("update_product_color/<int:pid>/",
         views.UpdateProductColour.as_view(), name="update-product-color"),

    path('add_product_image/', views.AddproductImage.as_view(),
         name="add_product_image"),
    path("update_product_image/<int:pid>/",
         views.UpdateProductImage.as_view(), name="update-product-image"),

    path('add_product_brand/', views.AddBrands.as_view(), name="add-product-brand"),
    path("update_product_brand/<int:pk>/",
         views.BrandUpdate.as_view(), name="update-brand"),

    path("add_specifications/", views.AddProductSpecification.as_view(),
         name="add-specifications"),
    path("get_spefications/<int:pid>/",
         views.ViewProductSpefications.as_view(), name="get-spefications"),
    path("update_product_specification/<int:pk>/",
         views.ProductSpeficationsUpdate.as_view(), name="update-product-specification"),
    path('view_orders/', views.ViewOrders.as_view(),
         name="view-order"),
    path('view_store/', views.GetStore.as_view(),
         name="view-store"),
    path('add_category/',views.AddCategories.as_view(), name='add-category'),
     path('update_category/<int:pk>/',
         views.CategoriesUpdate.as_view(), name="update-category"),
    path('view_product_category/<int:pid>/',
         views.ProductCategoriesview.as_view(), name="view-product-category"),
    path('get_category/<int:pk>/',
         views.CategoriesGet.as_view(), name="Get-category"),
    path('store_wise_product/<int:sid>/', views.ProductStoreWiseView.as_view(),
         name="store-wise-product"),

     path('add_product_subproduct/', views.AddProductSubProduct.as_view(),
         name="add-product-subproduct"),
     path("update_product_subproduct/<int:pk>/",
         views.UpdateProductSubProduct.as_view(), name="update-product-subproduct"),
]
