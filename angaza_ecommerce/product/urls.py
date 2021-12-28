from django.urls import path, include
from .views import *
from users import views

urlpatterns = [

     path('check_sale/', CheckSale.as_view(), name="check_sale"),
     path('create_deals/', DealsAdd.as_view(), name="create_deals"),
     path('view_feature_Deal/', GetFeatureDealProduct.as_view(), name="feature-Deal"),
     path('view_recent_Deal/', GetRecentDealProduct.as_view(), name="recent-Deal"),
     path('view_popular_Deal/', GetPopularDealProduct.as_view(), name="popular-Deal"),
     path('view_deal_of_the_month/', GetDealOfTheMonthProduct.as_view(), name="view-deal-of-the-month"),
     path('view_products_image/<int:pid>/', ViewProductImage.as_view(), name="view_products_image"),
     path('add_cart/', CartAdd.as_view(), name="add-cart"),

     path('view_cart_item/', GetCartProduct.as_view(), name="view-cart"),
     path('view_cart_buy_item/', GetCartBuyProduct.as_view(), name="view-cart-buy"),
     path('view_cart_book_item/', GetCartBookProduct.as_view(), name="view-cart-book"),

     path('remove_cart_item/<int:pk>/',RemoveCartItem.as_view(), name="remove-cart-item"),
     path('view_product_size/<int:pid>/',ViewProductSize.as_view(), name="view-size"),
     path('add_review/', ProductReviewAdd.as_view(), name="add-review"),
     path('view_review_item/<int:pid>/',GetProductReview.as_view(), name="view-review"),
     path('update_review/<int:pk>/',UpdateProductReview.as_view(), name="update-cart"),
     path('add_wishlist/', AddWishList.as_view(), name="add-wishlist"),
     path('view_wishlist_item/<int:uid>/',GetWishListProduct.as_view(), name="view-wishlist"),
     path('remove_wishlist_item/<int:pk>/',ItemRemoveWishlist.as_view(), name="remove-wishlist"),
     path('view_products/', ProductView.as_view(), name="view_products"),
     path('view_product_details/<int:pk>/',ProductDetailsView.as_view(), name="view_product_details"),
     path('search_product', DealSearch.as_view(), name="product-search"),
     path('category_list/', CategoriesProduct.as_view(), name="category_list"),
     path("category_wise_list/<int:cid>/",CategoriesWiseDeal.as_view(), name="category_wise_list"),
     path('view_description/<int:pid>/',GetProductDescription.as_view(), name="view-description"),
     path('add_question/', AddProductQuestions.as_view(), name="add-question"),
     path("view_question/<int:pid>/",GetProductQuestion.as_view(), name="view-question"),
     path("update_question/<int:pk>/",UpdateProductQuestion.as_view(), name="update-question"),
     path("product_colors_view/<int:pid>/",ViewProductColour.as_view(), name="product-colors-view"),
     path("view_subcategory/<int:cid>/", GetSubcategories.as_view(), name="view-subcategory"),
     path('slider-image/', SliderView.as_view(), name='slider-image'),
     path("cart_total_amount/<int:uid>/",CartTotalAmount.as_view(), name="cart-total-amount"),

     path("cart_total_book_amount/",CartTotalBookingAmount.as_view(), name="cart-total-book-amount"),
     path("cart_total_buy_amount/",CartTotalBuyAmount.as_view(), name="cart-total-buy-amount"),

     path("related_product/<int:pk>/",RelatedProduct.as_view(), name='related-product'),
     path("cart_quantity/<int:pid>/",CartQuantityMange.as_view(), name='cart-quantity'),  

     path("view_tag/",TagView.as_view(), name='view-tag'),
     path("view_brand/",BrandView.as_view(), name='view-brand'),
     path("view_own_product/",ViewOwnProduct.as_view(), name='view-own-product'),
     path("view_color/",ColourView.as_view(), name='view-color'),
     path("view_size/",SizeView.as_view(), name='view-size'),
     path("view_subproduct/",SubProductView.as_view(),name='view_subproduct'),
     path('view_product_subproduct/<int:pid>/',ViewProductSubProduct.as_view(), name="view-subproduct"),

     

     # cat with sub
     path('categories/',GetCatwithSub.as_view(),name='allcatnsub'),
     path('sub_categories_wise_deal/<int:cid>/',SubCategoriesWiseDeal.as_view(),name='sub-category-wise-deal')



]    
