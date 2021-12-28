from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from Notifications.models import Notification
from product.models import Cart, Product
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from stores.serializers import OrderProductSerializer
from users.models import Customer
from .models import Bill, BookingForm, Order, OrderProduct, SubBill
from .serializers import (BillSerializer, CreateBookingSerializer,
                          GetBookingSerializer, GetOrderSerializer,
                          OrderProductSerializer, OrderSerializer,
                          SubBillSerializer)


class OrderAdd(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OrderSerializer

    def post(self, request):
        request.data['customer'] = request.user.id
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            products = request.data['products']
            quantity_data = request.data['quantity']
            orders = Order.objects.get(pk=serializer.data["id"])
            i = 0
            discount = 0
            MRP = 0
            Total = 0
            product_name =[]
            for product_item in products:
                product = Product .objects.get(pk=product_item)
                discount += (product.price - product.sale_price)*quantity_data[i]
                MRP +=(product.price)*quantity_data[i]
                Total +=  (product.sale_price)*quantity_data[i]
                order_products=OrderProduct(product=product,order=orders,quantity=quantity_data[i])
                order_products.save()
                product.depot = product.depot-quantity_data[i]
                product.save()
                notification_title = f"You have recieved a new order {product.title} quality {quantity_data[i]} From {request.user.email}"
                Notification.objects.create(user=product.store.owner,title=notification_title,category="sale")
                SubBill.objects.create(customer=request.user,order_product=order_products,discount_price=(product.price - product.sale_price)*quantity_data[i],MRP_price=(product.price)*quantity_data[i],total_price=((product.price)*quantity_data[i])-((product.price - product.sale_price)*quantity_data[i]))
                i +=1
                product_name.append(product.title)
                if Cart.objects.filter(user__id=request.user.id,product__id=product_item).exists():
                    cart=Cart.objects.filter(user__id=request.user.id,product__id=product_item)
                    cart.delete()
            params ={"product_name":product_name,"first_name":request.user.first_name,"last_name":request.user.last_name}
            email_message = render_to_string("templates/order.html",params)
            send_mail("Successfully Product Order", "Order Product", settings.EMAIL_HOST_USER, [orders.customer.email], html_message = email_message)
            if orders.buy==True:
                Bill.objects.create(customer=request.user,order=orders,discount_price=discount,MRP_price=MRP,total_price=Total)
            Notification.objects.create(user=request.user,title=f"You have order {product_name} successfully",category="purchase")
            sender = settings.EMAIL_HOST_USER
            return Response({"data": serializer.data, "sucess": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "sucess": False})


class GetAllOneUserOrder(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = GetOrderSerializer

    def get_object(self, uid):
        try:
            return Order.objects.filter(customer__id=uid, order_cancel=False)
        except Order.DoesNotExist:
            raise Http404


    def get(self, request):
        orders = self.get_object(request.user.id) 
        serializer = GetOrderSerializer(orders,many=True)
        orders_data = serializer.data
        for order_data in orders_data:
            order_product = OrderProduct.objects.filter(order__id=order_data['id'])
            order_list = []
            quantity_list = []
            price_list = []
            for one_order in order_product:
                order_list.append(one_order.product.title)
                quantity_list.append(one_order.quantity)
                price_list.append(one_order.product.sale_price)
            order_data["orders"] = order_list
            order_data["quantity"]=quantity_list
            order_data["price"]=price_list
        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "sucess": True})



class CancelOrder(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OrderSerializer

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk, order_cancel=False)
        except Order.DoesNotExist:
            raise Http404

    def order_get(self,pk):
        try:
            return OrderProduct.objects.filter(order__id=pk)
        except OrderProduct.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        orders = self.get_object(pk)
        if request.user.id == orders.customer.id or request.user.is_superuser or request.user.role == 2 or request.user.role == 3:
            orders.order_cancel = True
            orders.delivered_date = None
            orders.save()
            order_products = self.order_get(pk)
            product_item = []
            for op in order_products:
                product_item.append(op.product.title)
                params ={"product_name":op.product.title,"order_id":op.id}
                email_message = render_to_string("templates/cancel_order_store.html",params)
                send_mail("Customer Cancel Order", "Order cancel", settings.EMAIL_HOST_USER, [op.product.store.owner.email], html_message = email_message)
                op.status="Declain"
                op.save()
            params ={"product_name":product_item,"username":request.user.username}
            email_message = render_to_string("templates/cancel_order.html",params)
            send_mail("Successfully Cancel Order", "Order cancel", settings.EMAIL_HOST_USER, [orders.customer.email], html_message = email_message)
            Notification.objects.create(user=request.user,title = f"you have successfully {product_item} cancel order",category="order cancel")
            return Response({"message": "Successfully Cancel Order", "status": status.HTTP_201_CREATED, "sucess": True})
        return Response({"message": "You don't permission Cancel order", "success": False})


class ViewAllOneUserCancelOrder(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = OrderSerializer

    def get_object(self, uid):
        try:
            return OrderProduct.objects.filter(order__customer__id=uid, order__order_cancel=True)
        except OrderProduct.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        cancel_orders = self.get_object(request.user.id)
    
        serializer = OrderProductSerializer(cancel_orders, many=True)
        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "sucess": True})


class ViewCancelOrderDetails(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = OrderProductSerializer

    def get_object(self, pk):
        try:
            return OrderProduct.objects.get(pk=pk, order_cancel=True)
        except OrderProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cancel_order = self.get_object(pk)
        if request.user.id == cancel_order.order.customer.id or  request.user.id == cancel_order.product.store.owner.id:
            serializer = OrderProductSerializer(cancel_order)
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "sucess": True})
        return Response({"message": "You don't permission View cancel order details", "success": False})




class OrderSales(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get_object(self, pid):
        try:
            number_of_sales = OrderProduct.objects.filter(product__id=pid,order__order_cancel=False).count()
            return number_of_sales
        except Order.DoesNotExist:
            number_of_sales = 0
            return number_of_sales

    def get(self, request, pid):
        numberofsales = self.get_object(pid)
        return Response({"numberofsales": numberofsales, "sucess": True})




class ViewBillOrderWise(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BillSerializer

    def get_object(self, oid):
        try:
            return Bill.objects.get(order__id=oid)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, oid):
        bill = self.get_object(oid)
        serializer = BillSerializer(bill)
        bill_data = serializer.data
        order_product = OrderProduct.objects.filter(order__id=oid)
        order_list = []
        quantity_list = []
        price_list = []
        product_status =[]
        for one_order in order_product:
            order_list.append(one_order.product.title)
            quantity_list.append(one_order.quantity)
            price_list.append(one_order.product.sale_price)
            product_status.append(one_order.status)
        bill_data["orders"] = order_list
        bill_data["quantity"]=quantity_list
        bill_data["price"]=price_list
        bill_data['product_status']=product_status
        return Response({"data": bill_data, "status": status.HTTP_201_CREATED, "sucess": True})



class OrderAction(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self, pk):
        try:
            return OrderProduct.objects.get(pk=pk, order__order_cancel=False)
        except OrderProduct.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        orders = self.get_object(pk)
        orders.status = request.data["status"]
        orders.save()
        print('orders orders-->',orders.order.id)
        Order.objects.filter(id=orders.order.id).update(status=request.data["status"])
        if orders.status=="Declain":
            params = {"product":orders.product}
            email_message = render_to_string("templates/order_declain.html",params)
            send_mail("Order Declain", "Order Declain", settings.EMAIL_HOST_USER, [orders.order.customer.email], html_message = email_message)
            Notification.objects.create(user=request.user,title = f"you have successfully {orders.product} declain order",category="order decalin")
        if orders.status=="Accept":
            Notification.objects.create(user=request.user,title = f"you have successfully {orders.product} accept order",category="order accept")
        return Response({"message": f"Order Successfully {orders.status}", "status": status.HTTP_201_CREATED, "sucess": True})



class BookingFormAdd(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateBookingSerializer

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk, order_cancel=False)
        except Order.DoesNotExist:
            raise Http404


    def post(self, request):
        orders =  self.get_object(request.data['order'])
        print(request.data)
        print(orders)
        serializer = CreateBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class ViewBookingForm(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BillSerializer

    def get_object(self, oid):
        try:
            return BookingForm.objects.get(order__id=oid)
        except BookingForm.DoesNotExist:
            raise Http404

    def get(self, request, oid):
        bookingform = self.get_object(oid)
        serializer = GetBookingSerializer(bookingform)
        book_data = serializer.data
        order_product = OrderProduct.objects.filter(order__id=oid)
        order_list = []
        quantity_list = []
        price_list = []
        product_status = []
        for one_order in order_product:
            order_list.append(one_order.product.title)
            quantity_list.append(one_order.quantity)
            price_list.append(one_order.product.sale_price)
            product_status.append(one_order.status)
        book_data["orders"] = order_list
        book_data["quantity"]=quantity_list
        book_data["price"]=price_list
        book_data["product_status"]=product_status
        return Response({"data":book_data, "status": status.HTTP_201_CREATED, "sucess": True})


class ViewSubBill(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SubBillSerializer

    def get_object(self, oid):
        try:
            return SubBill.objects.get(order_product__id=oid)
        except SubBill.DoesNotExist:
            raise Http404

    def get(self, request, oid):
        bill = self.get_object(oid)
        serializer = SubBillSerializer(bill)
        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "sucess": True})


class UpdateBookingForm(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self, pk):
        try:
            return BookingForm.objects.get(pk=pk)
        except BookingForm.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_review = self.get_object(pk)
        serializer = GetBookingSerializer(product_review)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        bookingform = self.get_object(pk)
        if bookingform.order.customer.id == request.user.id:
            request.data['order'] = bookingform.order.id
            serializer = CreateBookingSerializer(bookingform, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "You don't permission update booking Form", "success": False})



class ViewOrderDetails(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self, oid):
        try:
            return OrderProduct.objects.filter(order__id=oid)
        except OrderProduct.DoesNotExist:
            raise Http404

    def get(self, request, oid):
        order_item = self.get_object(oid)
        serializer = OrderProductSerializer(order_item,many=True)
        return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "sucess": True})
