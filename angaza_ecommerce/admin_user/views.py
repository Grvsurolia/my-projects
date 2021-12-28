from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from product.models import (Brand, Category, Colour, Deal, Size, SubCategories, SubProduct,
                            WishList)
from product.serializers import (BrandSerializer, CategoriesSerializer,
                                 ColoursSerializer, DealsSerializer,
                                 ProductDealSerializer, SizeSerializer,
                                 SubCategorySerializer, SubProductSerializer)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from users.models import User
from validate_email import validate_email

from admin_user.models import (AdminUser, DetailPagesAdvertisement,
                               HomePagesAdvertisement)

from .serializers import (AdminUserSerializer,
                          DetailPagesAdvertisementSerializer,
                          HomePagesAdvertisementSerializer)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{6,18}$"


# class AddSubproduct(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, ]
#     serializer_class = SubProductSerializer

#     def post(self, request):
#         if request.user.is_superuser or request.user.role == 2 or request.user.role==3:
#             serializer = SubProductSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"data": serializer.data, "success": True})
#             return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
#         return Response({"message": "you don't have permissions for Add Size", "success": False})

# class SubProductUpdate(generics.RetrieveUpdateAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = SubProductSerializer

#     def get_object(self, pk):
#         try:
#             return SubProduct.objects.get(pk=pk)
#         except SubProduct.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         subproduct = self.get_object(pk)
#         serializer = SubProductSerializer(subproduct)
#         return Response({"data": serializer.data, "success": True})

#     def put(self, request, pk, format=None):
#         subproduct = self.get_object(pk)
#         if request.user.is_superuser or request.user.role == 2:
#             serializer = SubProductSerializer(subproduct, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"data": serializer.data, "success": True})
#             return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
#         return Response({"message": "you don't have permissions for update size", "success": False})


class AddSize(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SizeSerializer

    def post(self, request):
        if request.user.is_superuser or request.user.role == 2 or request.user.role==3:
            serializer = SizeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Size", "success": False})


class SizeUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SizeSerializer

    def get_object(self, pk):
        try:
            return Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        size = self.get_object(pk)
        serializer = SizeSerializer(size)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        size = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2:
            serializer = SizeSerializer(size, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update size", "success": False})


class AddColours(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ColoursSerializer

    def post(self, request):
        if request.user.role == 2 or request.user.is_superuser or request.user.role==3:
            serializer = ColoursSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Colours", "success": False})


class ColoursUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ColoursSerializer

    def get_object(self, pk):
        try:
            return Colour.objects.get(pk=pk)
        except Colour.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        colour = self.get_object(pk)
        serializer = ColoursSerializer(colour)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        colour = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or request.user.role==3:
            serializer = ColoursSerializer(colour, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update colour", "success": False})


class AddBrands(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BrandSerializer

    def post(self, request):
        if request.user.is_superuser or request.user.role == 2 or request.user.role==3:
            request.data['user']=request.user.id
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "sucess": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "sucess": False})
        return Response({"message": "you don't have permissions for add Brand", "success": False})


class BrandUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BrandSerializer

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response({"data": serializer.data, "sucess": True})

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or request.user.role== 3:
            request.data['user']=request.user.id
            serializer = BrandSerializer(brand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "sucess": False})
        return Response({"message": "you don't have permissions for update Brand", "sucess": False})



class AddHomePagesAdvertisement(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = HomePagesAdvertisementSerializer

    def post(self, request):
        if request.user.role == 2 or request.user.is_superuser:
            serializer = HomePagesAdvertisementSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Home page ", "success": False})



class HomePagesAdvertisementUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = HomePagesAdvertisementSerializer

    def get_object(self, pk):
        try:
            return HomePagesAdvertisement.objects.get(pk=pk)
        except HomePagesAdvertisement.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        adv = self.get_object(pk)
        serializer = HomePagesAdvertisementSerializer(adv)
        return Response({"data": serializer.data, "sucess": True})

    def put(self, request, pk, format=None):
        adv = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2:
            serializer = HomePagesAdvertisementSerializer(
                adv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "sucess": False})
        return Response({"message": "you don't have permissions for update Brand", "sucess": False})



class AddDeatilPagesAdvertisement(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DetailPagesAdvertisementSerializer

    def post(self, request):
        if request.user.role == 2 or request.user.is_superuser:
            serializer = DetailPagesAdvertisementSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Detail page advertisement", "success": False})


class DeatilPagesAdvertisementUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DetailPagesAdvertisementSerializer

    def get_object(self, pk):
        try:
            return DetailPagesAdvertisement.objects.get(pk=pk)
        except DetailPagesAdvertisement.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        adv = self.get_object(pk)
        serializer = DetailPagesAdvertisementSerializer(adv)
        return Response({"data": serializer.data, "sucess": True})

    def put(self, request, pk):
        adv = self.get_object(pk)
        if request.user.id == 2 or request.user.is_superuser:
            serializer = DetailPagesAdvertisementSerializer(
                adv, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update Detail page advertisement", "success": False})



class ViewAllHomePagesAdvertisement(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomePagesAdvertisementSerializer

    def get_object(self):
        try:
            return HomePagesAdvertisement.objects.filter(status=True)
        except HomePagesAdvertisement.DoesNotExist:
            raise Http404

    def get(self, request):
        adv = self.get_object()
        serializer = HomePagesAdvertisementSerializer(adv, many=True)
        return Response({"data": serializer.data, "sucess": True})




class ViewNumberWiseDetailPagesAdvertisement(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DetailPagesAdvertisementSerializer
    # queryset = DetailPagesAdvertisement.objects.first()

    def get(self, request):
        # adv = self.get_object(inumber)
        adv = DetailPagesAdvertisement.objects.first()
        serializer = DetailPagesAdvertisementSerializer(adv)
        return Response({"data": serializer.data, "sucess": True})


class ProductConnectWithDeal(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductDealSerializer

    def post(self, request):
        if request.user.role == 2 or request.user.is_superuser:
            serializer = ProductDealSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "Only admin and superuser connect product to deal", "success": False})



