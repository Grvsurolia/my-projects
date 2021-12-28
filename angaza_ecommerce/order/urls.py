from django.urls import path
from django.contrib.auth import views
from .import views

urlpatterns = [
    path('add_orderitem/', views.OrderAdd.as_view(), name="add-orderitem"),
    path('view_own_order/',
         views.GetAllOneUserOrder.as_view(), name="view-orderitem"),
    path('cancel_order/<int:pk>/', views.CancelOrder.as_view(), name="cancel-order"),
    path('Viewall_cancel_order/<int:uid>/',
         views.ViewAllOneUserCancelOrder.as_view(), name="cancel-item"),
    path('cancel_order_detail/<int:pk>/',
         views.ViewCancelOrderDetails.as_view(), name="cancel-item"),

    path('product_sale/<int:pid>/',
         views.OrderSales.as_view(), name="all-cancel-item"),
    path('view_bill/<int:oid>/', views.ViewBillOrderWise.as_view(), name="view-bill"),
    path('order_action/<int:pk>/', views.OrderAction.as_view(), name="view-action"),

    path('add_bookinform/', views.BookingFormAdd.as_view(), name="add-bookinform"),
    path('view_booking_form/<int:oid>/',
         views.ViewBookingForm.as_view(), name="view-booking-form"),
    path('view_subbill/<int:oid>/',
         views.ViewSubBill.as_view(), name="view-subbill"), 
    path('update_booking_form/<int:pk>/', views.UpdateBookingForm.as_view(), name="update-booking-form"),
    path("order_detail/<int:oid>/", views.ViewOrderDetails.as_view(), name="order-detail")

]
