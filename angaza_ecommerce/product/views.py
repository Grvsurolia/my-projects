import datetime
import re
from enum import unique
from itertools import chain, product

from django.db.models import Q, manager
from django.http import HttpResponse, JsonResponse, response
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import generics, permissions, serializers, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from stores.serializers import ProductSpecificationSerializer

from .models import (Brand, Cart, Category, Colour, Deal, Product,
                     ProductCategory, ProductColour, ProductDeal,
                     ProductDescription, ProductImage, ProductQuestion,
                     ProductReview, ProductSize, Size, Slider, Specification,
                     Store, SubCategories, SubProduct, Tag, WishList)
from .serializers import (BrandSerializer, CartCreateSerializer,
                          CartSerializer, CategoriesSerializer,
                          ColoursSerializer, DealsSerializer,
                          GetCatgoriesSerializer, ProductCategorySerializer,
                          ProductCategorySerializer1, ProductColourSerializer,
                          ProductDealSerializer, ProductDescriptionSerializer,
                          ProductDetailSerializer, ProductImageSerializer,
                          ProductQuestionSerializer, ProductReviewSerializer,
                          ProductSerializer, ProductSizeSerializer,
                          SizeSerializer, SliderSerializer,
                          SpecificationSerializer, SubCategorySerializer, SubProductSerializer,
                          TagSerializer, WishListCreateSerializer,
                          WishListSerializer)


class DealsAdd(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        if request.user.role == 2 or request.user.is_superuser:
            data = JSONParser().parse(request)
            serializer = DealsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': "please Activate/Verify Your account", 'status': status.HTTP_200_OK})


class GetFeatureDealProduct(APIView):
    permission_classes = (permissions.AllowAny,)
 
    def get_objects(self):
        try:
            return ProductDeal.objects.filter(product_deals__name="FeatureDeal")
        except ProductDeal.DoesNotExist:
            return Http404

    def get(self, request):
        all_feature_deal = self.get_objects()
        serializer = ProductDealSerializer(all_feature_deal, many=True)
        feature_deal_data = serializer.data
        for prod_data in feature_deal_data:
            prod_id = prod_data['product']['id']
            prod_category = ProductCategory.objects.filter(
                product=prod_id)
            category_list = []
            for cat in prod_category:
                if cat.product_sub_category=="" or cat.product_sub_category==None or cat.product_sub_category=={}:
                    category_list.append(cat.product_category.name)
                else:
                    category_list.append(cat.product_sub_category.sub_name)
            prod_data["category"] = category_list
        return Response({"data": serializer.data, "success": True})


class GetDealOfTheMonthProduct(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self):
        try:
            return ProductDeal.objects.filter(product_deals__name="DealOfTheMonth")
        except ProductDeal.DoesNotExist:
            return Http404

    def get(self, request):
        all_feature_deal = self.get_objects()
        serializer = ProductDealSerializer(all_feature_deal, many=True)
        dealofthemonth = serializer.data
        for prod_data in dealofthemonth:
            prod_id = prod_data['product']['id']
            prod_category = ProductCategory.objects.filter(
                product=prod_id)
            category_list = []
            for cat in prod_category:
                if cat.product_sub_category=="" or cat.product_sub_category==None or cat.product_sub_category=={}:
                    category_list.append(cat.product_category.name)
                else:
                    category_list.append(cat.product_sub_category.sub_name)
            prod_data["category"] = category_list
        return Response({"data": serializer.data, "success": True})






today = datetime.datetime.today()
class GetRecentDealProduct(APIView):
    permission_classes = (permissions.AllowAny,)



    def get(self, request):
        print(request.GET['filter'],"this is gate")
        if request.GET['filter']=="order_by_date":
            all_recent_deal = Product.objects.filter(end_time__gte=today).order_by("-created_at")
            serializer = ProductSerializer(all_recent_deal, many=True)
            feature_deal_data = serializer.data
            for prod_data in feature_deal_data:

                prod_id = prod_data['id']
                prod_category = ProductCategory.objects.filter(
                    product=prod_id)
                category_list = []
                for cat in prod_category:
                    if cat.product_sub_category=="" or cat.product_sub_category==None or cat.product_sub_category=={}:
                        category_list.append(cat.product_category.name)
                    else:
                        category_list.append(cat.product_sub_category.sub_name)
                prod_data["category"] = category_list
            t = []
            for i in serializer.data:
                f = {
                        "id":i['id'],
                        "product":i
                    }
                
                t.append(f)
            return Response({"data":list(t), "success": True})
            return Response({"data":serializer.data, "success": True})
        elif request.GET['filter']=="order_by_descending":
            all_recent_deal = Product.objects.filter(end_time__gte=today).order_by("id")
            serializer = ProductSerializer(all_recent_deal, many=True)
            feature_deal_data = serializer.data
            for prod_data in feature_deal_data:

                prod_id = prod_data['id']
                prod_category = ProductCategory.objects.filter(
                    product=prod_id)
                category_list = []
                for cat in prod_category:
                    if cat.product_sub_category=="" or cat.product_sub_category==None or cat.product_sub_category=={}:
                        category_list.append(cat.product_category.name)
                    else:
                        category_list.append(cat.product_sub_category.sub_name)
                prod_data["category"] = category_list
            t = []
            for i in serializer.data:
                f = {
                        "id":i['id'],
                        "product":i
                    }
                
                t.append(f)
            return Response({"data":list(t), "success": True})
            return Response({"data":serializer.data, "success": True})
        else:
            pass


class GetPopularDealProduct(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self):
        try:
            return ProductDeal.objects.filter(product_deals__name="PopularDeal")
        except ProductDeal.DoesNotExist:
            return Http404

    def get(self, request):
        # deals = self.get_objects()
        # serializer = ProductDealSerializer(deals, many=True)
        # return Response({"data": serializer.data, "success": True})

        all_popular_deal = self.get_objects()
        serializer = ProductDealSerializer(all_popular_deal, many=True)
        feature_deal_data = serializer.data
        for prod_data in feature_deal_data:
            prod_id = prod_data['product']['id']
            prod_category = ProductCategory.objects.filter(
                product=prod_id)
            category_list = []
            for cat in prod_category:
                if cat.product_sub_category=="" or cat.product_sub_category==None or cat.product_sub_category=={}:
                    category_list.append(cat.product_category.name)
                else:
                    category_list.append(cat.product_sub_category.sub_name)
            prod_data["category"] = category_list
        return Response({"data": serializer.data, "success": True})


class ProductView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response({"data": serializer.data, "success": True})


class ProductDetailsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, pk):
        product = self.get_objects(pk)
        product.visit_product += 1
        product.save()
        serializer = ProductDetailSerializer(product)
        product_data = serializer.data
        categories = ProductCategory.objects.filter(product=pk)
        all_categories = []
        for category in categories:
            if category.product_sub_category=="" or category.product_sub_category==None or category.product_sub_category=={}:
                all_categories.append(category.product_category.name)
            else:
               all_categories.append(category.product_sub_category.sub_name) 
        resp = {
            "product": product_data,
            "categories": all_categories
        }
        return Response({"data": resp, "success": True})


class ProductSpecification(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return False

    def get(self, request, pk):
        product = self.get_objects(pk)
        colors = []
        sizes = []
        if product:
            pcolor = ProductColour.objects.filter(product=pk).exists()
            if pcolor:
                productcolor = ProductColour.objects.filter(product=pk)
                for colour in productcolor:
                    colors.append(colour.product_color.name)
            psize = ProductSize.objects.filter(product=pk).exists()
            if psize:
                prouductsize = ProductSize.objects.filter(product=pk)
                for size in prouductsize:
                    sizes.append(size.product_size.size_or_weight)
            resp = {
                "colors": colors,
                "sizes": sizes,
                "brand": product.brand.name
            }
            return Response({"data": resp, "success": True})
        return Response({"message": "Product not Available", "success": False})


class DealSearch(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        tosearch = request.GET.get("search")
        tries = []
        pc_id = []
        if tosearch:
            products = ProductCategory.objects.filter(Q(product__title__icontains=tosearch) | Q(product__description__icontains=tosearch) | Q(product_category__name__icontains=tosearch) | Q(
                product__store__name__icontains=tosearch) | Q(product__brand__name__icontains=tosearch)| Q(product_category__subcategory__sub_name__icontains=tosearch)| Q(product__store__location__icontains=tosearch)).distinct()
            for product in products:
                if product.product.id in tries:
                    pass
                else:
                    tries.append(product.product.id)
                    pc_id.append(product.id)
            filter_product=ProductCategory.objects.filter(pk__in=pc_id)
            serializer = ProductCategorySerializer1(filter_product, many=True)
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        else:
            products = ProductCategory.objects.all()
            for product in products:
                if product.product.id in tries:
                    pass
                else:
                    tries.append(product.product.id)
                    pc_id.append(product.id)
            filter_product=ProductCategory.objects.filter(pk__in=pc_id)
            serializer = ProductCategorySerializer1(filter_product, many=True)
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})


class ViewProductImage(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pid):
        try:
            return ProductImage.objects.filter(product__id=pid)
        except ProductImage.DoesNotExist:
            return Http404

    def get(self, request, pid):
        product_image = self.get_objects(pid)
        serializer = ProductImageSerializer(product_image, many=True)
        return JsonResponse(serializer.data, safe=False)


class ViewProductSize(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pid):
        try:
            return ProductSize.objects.filter(product__id=pid)
        except ProductSize.DoesNotExist:
            return Http404

    def get(self, request, pid):
        product_size = self.get_objects(pid)
        serializer = ProductSizeSerializer(product_size, many=True)
        return JsonResponse(serializer.data, safe=False)


class ViewProductColour(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pid):
        try:
            return ProductColour.objects.filter(product__id=pid)
        except ProductColour.DoesNotExist:
            return Http404

    def get(self, request, pid):
        product_size = self.get_objects(pid)
        serializer = ProductColourSerializer(product_size, many=True)
        return JsonResponse(serializer.data, safe=False)


class CartAdd(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartCreateSerializer

    def get_object(self, uid, pid):
        try:
            return Cart.objects.get(user__id=uid, product__id=pid)
        except Cart.DoesNotExist:
            return False

    def post(self, request):
        cart_available = self.get_object(
            request.user.id, request.data['product'])
        if cart_available:
            cart_available.quantity += 1
            cart_available.save()
            serializer = CartCreateSerializer(cart_available)
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        request.data['user'] = request.user.id
        serializer = CartCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class CartQuantityMange(generics.RetrieveAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self, uid, pid):
        try:
            return Cart.objects.get(user__id=uid, product__id=pid)
        except Cart.DoesNotExist:
            raise Http404

    def put(self, request, pid):
        user_id = request.user.id
        cart_item = self.get_object(user_id, pid)
        new_quantity = request.data['quantity']

        if new_quantity == 0:
            cart_item.delete()
            return Response({"data": "Product successfully delete in cart", "success": True})
        else:
            cart_item.quantity = new_quantity
            cart_item.save()
            serializer = CartSerializer(cart_item)
            return Response({"data": serializer.data, "success": True})


class GetCartProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request):
        cart_item = self.get_object(request.user.id)
        serializer = CartSerializer(cart_item, many=True)
        return Response({"data": serializer.data, "success": True})


class GetCartBuyProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid,product__product_option="Buy")
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request):
        cart_item = self.get_object(request.user.id)
        serializer = CartSerializer(cart_item, many=True)
        return Response({"data": serializer.data, "success": True})


class GetCartBookProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid,product__product_option="Booking")
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request):
        cart_item = self.get_object(request.user.id)
        serializer = CartSerializer(cart_item, many=True)
        return Response({"data": serializer.data, "success": True})


class ProductReviewAdd(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductReviewSerializer

    def post(self, request):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class GetProductReview(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductReviewSerializer


    def get_object(self, pid):
        try:
            return ProductReview.objects.filter(deal__id=pid)
        except ProductReview.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        review = self.get_object(pid)
        serializer = ProductReviewSerializer(review, many=True)
        return Response({"data": serializer.data, "success": True})


class UpdateProductReview(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductReviewSerializer


    def get_object(self, pk):
        try:
            return ProductReview.objects.get(pk=pk)
        except ProductReview.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_review = self.get_object(pk)
        serializer = ProductReviewSerializer(product_review)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        product_review = self.get_object(pk)
        request.data['deal'] = product_review.deal.id
        serializer = ProductReviewSerializer(product_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})


class RemoveCartItem(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class= CartSerializer

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response({"data": serializer.data, "success": True})

    def delete(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        if request.user.is_superuser or request.user.id == cart_item.user.id or request.user.role == 2:
            cart_item.delete()
            return Response({"message": "Remove cart item", "success": True, "status": status.HTTP_204_NO_CONTENT})
        return Response({"message": "you don't have permissions", "success": False})


class AddWishList(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WishListCreateSerializer

    def get_object(self, uid, pid):
        try:
            return WishList.objects.get(user__id=uid, product__id=pid)
        except WishList.DoesNotExist:
            return False

    def post(self, request):
        wishlist_available = self.get_object(
            request.user.id, request.data['product'])
        if wishlist_available:
            return Response({"message": "Product already available in Wishlist", "success": False})
        request.data['user'] = request.user.id
        serializer = WishListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class GetWishListProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WishListSerializer

    def get_object(self, uid):
        try:
            return WishList.objects.filter(user__id=uid, is_delete=False)
        except WishList.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        wishlist_item = self.get_object(uid)
        if request.user.id == uid or request.user.role == 2 or request.user.is_superuser:
            serializer = WishListSerializer(wishlist_item, many=True)
            return Response({"data": serializer.data, "success": True})
        return Response({"message": "you don't have permissions ", "success": False})


class ItemRemoveWishlist(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WishListSerializer

    def get_object(self, pk):
        try:
            return WishList.objects.get(pk=pk)
        except WishList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        wishlist_item = self.get_object(pk)
        serializer = WishListSerializer(wishlist_item)
        return Response({"data": serializer.data, "success": True})

    def delete(self, request, pk, format=None):
        wishlist_item = self.get_object(pk)
        if request.user.is_superuser or request.user.id == wishlist_item.user.id or request.user.role == 2:
            wishlist_item.delete()
            return Response({"message": "Deal Successfully remove in Wish List ", "success": False})
        return Response({"message": "you don't have permissions ", "success": False})


class CategoriesProduct(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = GetCatgoriesSerializer


    def get_objects(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            return Http404

    def get(self, request):
        all_category = self.get_objects()
        serializer = GetCatgoriesSerializer(all_category, many=True)
        return Response({"data": serializer.data, "success": True})


class CategoriesWiseDeal(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductCategorySerializer1

    def get_objects(self, cid):
        try:
            return ProductCategory.objects.filter(product_category__id=cid)
        except ProductCategory.DoesNotExist:
            return Http404

    def get(self, request, cid):
        all_category = self.get_objects(cid)
        serializer = ProductCategorySerializer1(all_category, many=True)
        return Response({"data": serializer.data, "success": True})


class SubCategoriesWiseDeal(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductCategorySerializer1


    def get_objects(self, cid):
        try:
            return ProductCategory.objects.filter(product_sub_category__id=cid)
        except ProductCategory.DoesNotExist:
            return Http404

    def get(self, request, cid):
        all_category = self.get_objects(cid)
        serializer = ProductCategorySerializer1(all_category, many=True)
        return JsonResponse(serializer.data, safe=False)


class GetProductDescription(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductDescriptionSerializer

    def get_object(self, pid):
        try:
            return ProductDescription.objects.filter(product__id=pid)
        except ProductDescription.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        product_description = self.get_object(pid)
        serializer = ProductDescriptionSerializer(
            product_description, many=True)
        return Response({"data": serializer.data, "success": True})


class AddProductQuestions(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ProductQuestionSerializer


    def post(self, request):
        request.data['user'] = request.user.id
        if request.user.is_superuser or request.user.role == 2:
            serializer = ProductQuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions", "success": False})


class GetProductQuestion(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductQuestionSerializer

    def get_object(self, pid):
        try:
            return ProductQuestion.objects.filter(product__id=pid)
        except ProductQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        product_questions = self.get_object(pid)
        serializer = ProductQuestionSerializer(product_questions, many=True)
        return Response({"data": serializer.data, "success": True})


class UpdateProductQuestion(APIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ProductQuestionSerializer

    def get_object(self, pk):
        try:
            return ProductQuestion.objects.get(pk=pk)
        except ProductQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_questions = self.get_object(pk)
        serializer = ProductQuestionSerializer(product_questions)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        product_questions = self.get_object(pk)
        if request.user.id == 2 or request.user.is_superuser:
            request.data["user"] = product_questions.user.id
            request.data["product"] = product_questions.product.id
            serializer = ProductQuestionSerializer(
                product_questions, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions ", "success": False})




class GetSubcategories(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductCategorySerializer

    def get_object(self, cid):
        try:
            return SubCategories.objects.filter(category__id=cid)
        except SubCategories.DoesNotExist:
            raise Http404

    def get(self, request, cid):
        subcategory = self.get_object(cid)
        serializer = ProductCategorySerializer(subcategory, many=True)
        return Response({"data": serializer.data, "success": True})


class GetCatwithSub(generics.ListAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class=ProductCategorySerializer1
    
    def get_object(self):
        try:
            return ProductCategory.objects.all()
        except ProductCategory.DoesNotExist:
            raise Http404
    
    def get(self, request):
        cat = self.get_object()
        serializer = ProductCategorySerializer1(cat,many=True)
        return Response({"data":serializer.data})


class SliderView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()

    def post(self, request, *args, **kwargs):
        if request.user:
            serializer = SliderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        else:
            return Response({"error": "you don't have permission", "status": status.HTTP_400_BAD_REQUEST, "success": False})


class RelatedProduct(APIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        tags = product.tags.all()
        data = Product.objects.filter(tags__in=tags).distinct().exclude(id=pk)
        serializer = ProductSerializer(data, many=True)
        return Response({"data": serializer.data, "success": True})



class CartTotalAmount(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartSerializer

    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        cart_item = self.get_object(uid)
        total_amount = 0
        for one_item in cart_item:
            total_amount += (one_item.product.sale_price)*(one_item.quantity)
        return Response({"total_amount": total_amount, "success": True})


class CartTotalBookingAmount(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CartSerializer


    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid,product__product_option="Booking")
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request):
        cart_item = self.get_object(request.user.id)
        total_amount = 0
        for one_item in cart_item:
            total_amount += (one_item.product.sale_price)*(one_item.quantity)
        return Response({"total_amount": total_amount, "success": True})


class CartTotalBuyAmount(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CartSerializer


    def get_object(self, uid):
        try:
            return Cart.objects.filter(user__id=uid,product__product_option="Buy")
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request):
        cart_item = self.get_object(request.user.id)
        total_amount = 0
        for one_item in cart_item:
            total_amount += (one_item.product.sale_price)*(one_item.quantity)
        return Response({"total_amount": total_amount, "success": True})



class TagView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TagSerializer


    def get_object(self):
        try:
            return Tag.objects.all()
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request):
        tag = self.get_object()
        serializer = TagSerializer(tag, many=True)
        return Response({"data": serializer.data, "success": True})


class SizeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SizeSerializer


    def get_object(self):
        try:
            return Size.objects.all()
        except Size.DoesNotExist:
            raise Http404

    def get(self, request):
        size = self.get_object()
        serializer = SizeSerializer(size, many=True)
        return Response({"data": serializer.data, "success": True})


class BrandView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BrandSerializer

    def get_object(self,uid):
        try:
            return Brand.objects.filter(user__id=uid)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request):
        brand = self.get_object(request.user.id)
        serializer = BrandSerializer(brand, many=True)
        return Response({"data": serializer.data, "success": True})


class ColourView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ColoursSerializer

    def get_object(self):
        try:
            return Colour.objects.all()
        except Colour.DoesNotExist:
            raise Http404

    def get(self, request):
        colour = self.get_object()
        serializer = ColoursSerializer(colour, many=True)
        return Response({"data": serializer.data, "success": True})


class ViewOwnProduct(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductDetailSerializer

    def get_object(self, uid):
        try:
            return Product.objects.filter(store__owner__id=uid)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request):
        product = self.get_object(request.user.id)
        serializer = ProductDetailSerializer(product, many=True)
        return Response({"data": serializer.data, "success": True})


def HOME(request):
    "#Number of visits to this view, as counted in the session variable."
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits}
    return render(request,'templates\home.html',context=context)


class CheckSale(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        try:
            return Product.objects.filter(end_time__lte=today)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request):
        product_item = self.get_object()
        for one_item in product_item:
            one_item.is_sale=False
            one_item.save()
        return Response({"message": "successfully changes", "success": True})




class SubProductView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SubProductSerializer


    def get_object(self):
        try:
            return SubProduct.objects.all()
        except SubProduct.DoesNotExist:
            raise Http404

    def get(self, request):
        sub_product = self.get_object()
        serializer = SubProductSerializer(sub_product, many=True)
        return Response({"data": serializer.data, "success": True})


class ViewProductSubProduct(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_objects(self, pid):
        try:
            return SubProduct.objects.filter(product__id=pid)
        except SubProduct.DoesNotExist:
            return Http404

    def get(self, request, pid):
        product_subproduct = self.get_objects(pid)
        serializer = SubProductSerializer(product_subproduct, many=True)
        return JsonResponse(serializer.data, safe=False)