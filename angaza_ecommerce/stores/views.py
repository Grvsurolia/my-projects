import json
import ast
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, send_mail
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, response
from django.http.response import Http404
from django.views.decorators.csrf import csrf_exempt
from order.models import Order, OrderProduct
from product.models import (Brand, Category, Colour, Product, ProductCategory,
                            ProductColour, ProductDescription, ProductImage,
                            ProductQuestion, ProductSize, Size, Store, SubProduct)
from product.serializers import (BrandSerializer, GetCatgoriesSerializer,
                                 ProductCategorySerializer,
                                 ProductCategorySerializer1,
                                 ProductColourSerializer,
                                 ProductDescriptionSerializer,
                                 ProductImageSerializer, ProductSerializer,
                                 ProductSizeSerializer, SubProductSerializer)
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from users.serializers import UserSerializer
from validate_email import validate_email

from .models import ProductSpecification, StoreOwner
from .serializers import (GetOrderSerializer, GetProductCategoriesSerializer,
                          OrderProductSerializer,
                          ProductSpecificationSerializer, StoreSerializer)

# Create your views here.

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{6,18}$"



class AddStore(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StoreSerializer

    def post(self, request):
        request.data['owner'] = request.user.id
        if request.user.role == 3 or request.user.role == 2 or request.user.is_superuser:
            serializer = StoreSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                store = Store.objects.get(pk=serializer.data["id"])
                storeowner = StoreOwner(user=request.user,store=store)
                storeowner.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't able to add store", "success": True})


class StoreUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StoreSerializer

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        if request.user.id == store.owner.id or request.user.is_superuser or request.user.role == 2:
            request.data['owner'] = store.owner.id
            serializer = StoreSerializer(store, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
    

class AddProducts(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_colour(self,pk):
        try:
            return Colour.objects.get(pk=pk)
        except Colour.DoesNotExist:
            return False

    def get_size(self,pk):
        try:
            return Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return False
    
    # def get_subproduct(self,pk):
    #     try:
    #         return SubProduct.objects.get(pk=pk)
    #     except SubProduct.DoesNotExist:
    #         return False


    def post(self, request):
        if request.user.role == 2 or request.user.role == 3 or request.user.is_superuser or request.user.groups=="StoreOwner":
            request.data._mutable = True
            request.data["depot"]=request.data['inventory']
            request.data._mutable = False
            

            serializer = ProductSerializer(data=request.data)
            

            if serializer.is_valid():
                
                serializer.save()

                product = Product.objects.get(pk=serializer.data['id'])

                # subproduct_id = self.get_subproduct(request.data['sub_product'])
                # if subproduct_id:
                #     product_subproduct = ProductSubProduct(product=product, sub_product=subproduct_id)
                #     product_subproduct.save()

                color_id = self.get_colour(request.data['colour'])
                if color_id:
                    product_colour = ProductColour(product=product,product_color=color_id)
                

                    product_colour.save()
                product_size = self.get_size(request.data['size'])
                if product_size:
                    product_size=ProductSize(product=product,product_size=product_size)
                   

                    product_size.save()

                
                print("specfifcation ",type(json.loads(request.data["specification"])))
                ProductSpecification.objects.create(product=product,the_json=json.loads(request.data["specification"]))
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't permission add products", "success": False})



class ProductUpdate(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_objects(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get_colour(self,pk):
        try:
            return ProductColour.objects.get(product__id=pk)
        except ProductColour.DoesNotExist:
            raise False

    def get_size(self,pk):
        try:
            return ProductSize.objects.get(product__id=pk)
        except ProductSize.DoesNotExist:
            raise False
    
    def get_specification(self,pk):
        try:
            return ProductSpecification.objects.get(product__id=pk)
        except ProductSpecification.DoesNotExist:
            raise False

    # def get_subproduct(self,pk):
    #     try:
    #         return ProductSubProduct.objects.get(product__id=pk)
    #     except ProductSubProduct.DoesNotExist:
    #         raise False


    def get(self, request, pk):
        product = self.get_objects(pk)
        if product=={}:
            return Http404
        else:
            serializer = ProductSerializer(product)
            colour = ProductColour.objects.get(product__id=pk)
            size =  ProductSize.objects.get(product__id=pk)
            specification = ProductSpecification.objects.get(product__id=pk)
            # sub_product = ProductSubProduct.objects.get(product__id=pk)
            resp = {
                    "product":serializer.data,
                    "colour": colour.product_color.id,
                    "size": size.product_size.id,
                    "specification": specification.the_json,
                    # "sub_product":sub_product.sub_product.id
            }
            return Response({"data":json.dumps(resp), "success":True})
        

    def put(self, request, pk):
        product = self.get_objects(pk)
        if request.user.id == product.store.owner.id:
            request.data._mutable = True
            if request.data['thumbnail']=="" or request.data['thumbnail']==None:
                request.data["thumbnail"]=product.thumbnail
            request.data._mutable = False
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                productcolour = self.get_colour(pk)
                colour_id =int(request.data['colour'])
                colour = Colour.objects.get(id=colour_id)
                productcolour.product_color=colour
                productcolour.save()
                productsize = self.get_size(pk)
                size = Size.objects.get(pk=int(request.data['size']))
                productsize.product_size=size
                productsize.save()
                productspecification = self.get_specification(pk)
                productspecification.the_json=request.data['specification']
                productspecification.save()

                # subproduct_id =int(request.data['sub_product'])
                # subproduct = SubProduct.objects.get(id=subproduct_id)
                # subproduct.sub_product=subproduct
                # subproduct.save()

                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update cart", "success": False})


    def delete(self, request, pk, format=None):
        product = self.get_objects(pk)
        if request.user.is_superuser or request.user.id == product.store.owner.id or request.user.role == 2:
            product.delete()
            return Response({"message": "Remove product item", "success": True, "status": status.HTTP_204_NO_CONTENT})
        return Response({"message": "you don't have permissions for Remove Product Item", "success": False})


class AddProductDescription(generics.CreateAPIView):  
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductDescriptionSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except:
            return False

    def post(self, request):
        request_value = request.data.get('product')
        product_value = self.get_object(request_value)
        if product_value.store.owner.id == request.user.id or request.user.is_superuser or request.user.role == 2:
            serializer = ProductDescriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Product Description", "success": False})


class UpdateProductDescription(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductDescriptionSerializer

    def get_object(self, pk):
        try:
            return ProductDescription.objects.get(pk=pk)
        except ProductDescription.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_description = self.get_object(pk)
        serializer = ProductDescriptionSerializer(product_description)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        product_description = self.get_object(pk)
        serializer = ProductDescriptionSerializer(
            product_description, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
        return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})


class AddProductSize(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ProductSizeSerializer

    def post(self, request):
        product_id = request.data.get('product')
        proudcts = Product.objects.get(id=product_id)
        if request.user.role == 2 or request.user.id == proudcts.store.owner.id or request.user.is_superuser:
            serializer = ProductSizeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Product Size", "success": False})


class UpdateProductSize(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSizeSerializer

    def get_object(self, pk):
        try:
            return ProductSize.objects.get(pk=pk)
        except ProductSize.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_size = self.get_object(pk)
        serializer = ProductSizeSerializer(product_size)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        product_size = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or product_size.product.store.owner.id == request.user.id:
            serializer = ProductSizeSerializer(product_size, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update size", "success": False})


class AddProductColour(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductColourSerializer

    def post(self, request):
        product_id = request.data.get('product')
        proudcts = Product.objects.get(id=product_id)
        if request.user.role == 2 or request.user.id == proudcts.store.owner.id or request.user.is_superuser:
            serializer = ProductColourSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for Add Product colour", "success": False})


class UpdateProductColour(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductColourSerializer

    def get_object(self, pk):
        try:
            return ProductColour.objects.get(pk=pk)
        except ProductColour.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_colour = self.get_object(pk)
        serializer = ProductColourSerializer(product_colour)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        product_colour = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or product_colour.product.store.owner.id == request.user.id:
            serializer = ProductColourSerializer(
                product_colour, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update colour", "success": False})


class AddProductSubProduct(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = SubProductSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request):
        product = self.get_object(request.data.get("product"))
        if product.store.owner.id == request.user.id or request.user.is_superuser or request.user.role == 2:
            serializer = SubProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "sucess": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "sucess": False})
        return Response({"message": "you don't have permissions for Add Product image", "success": False})



class UpdateProductSubProduct(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SubProductSerializer

    def get_object(self, pk):
        try:
            return SubProduct.objects.get(pk=pk)
        except SubProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product_subproduct = self.get_object(pk)
        serializer = SubProductSerializer(product_subproduct)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        product_subproduct = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or product_subproduct.product.store.owner.id == request.user.id:
            serializer = SubProductSerializer(product_subproduct, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update subproduct", "success": False})

class AddproductImage(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductImageSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request):
        product = self.get_object(request.data.get("product"))
        if product.store.owner.id == request.user.id or request.user.is_superuser or request.user.role == 2:
            serializer = ProductImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "sucess": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "sucess": False})
        return Response({"message": "you don't have permissions for Add Product image", "success": False})


class UpdateProductImage(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductImageSerializer

    def get_object(self, pid):
        try:
            return ProductImage.objects.get(product__id=pid)
        except ProductImage.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        product_image = self.get_object(pid)
        serializer = ProductImageSerializer(product_image)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pid):
        product_image = self.get_object(pid)
        if request.user.id == product_image.product.store.owner.id or request.user.is_superuser or request.user.role == 2:
            request.data._mutable = True
            if request.data['product_image1']=="" or request.data['product_image1']==None:
                request.data["product_image1"]=product_image.product_image1
            if request.data['product_image2']=="" or request.data['product_image3']==None:
                request.data["product_image2"]=product_image.product_image3
            if request.data['product_image3']=="" or request.data['product_image3']==None:
                request.data["product_image3"]=product_image.product_image3
            if request.data['product_image4']=="" or request.data['product_image4']==None:
                request.data["product_image4"]=product_image.product_image4  
            request.data._mutable = False
            serializer = ProductImageSerializer(
                product_image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update Product images", "success": False})


class AddBrands(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BrandSerializer

    def post(self, request):
        if request.user.is_superuser or request.user.role == 2 or request.user.role==3:
            request.data['user']=request.user.id
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for add brand", "success": False})


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
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        brand = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2:
            serializer = BrandSerializer(brand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update Brand", "success": False})


class AddProductSpecification(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductSpecificationSerializer

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def post(self, request):
        product = self.get_object(request.data['product'])
        if request.user.is_superuser or request.user.role == 2 or product.store.owner.id == request.user.id:
            serializer = ProductSpecificationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for add brand", "success": False})


class ViewProductSpefications(APIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductSpecificationSerializer

    def get_object(self, pid):
        try:
            return ProductSpecification.objects.get(product__id=pid)
        except ProductSpecification.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        spefications = self.get_object(pid)
        print("type ",spefications.the_json)
        serializer = ProductSpecificationSerializer(spefications)
        return Response({"data": serializer.data, "success": True})


class ProductSpeficationsUpdate(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSpecificationSerializer

    def get_object(self, pk):
        try:
            return ProductSpecification.objects.get(pk=pk)
        except ProductSpecification.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        specification = self.get_object(pk)
        serializer = ProductSpecificationSerializer(specification)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        specification = self.get_object(pk)
        if request.user.id == specification.product.store.owner.id or request.user.is_superuser or request.user.role == 2:
            serializer = ProductSpecificationSerializer(
                specification, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions", "success": False})



class ViewOrders(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OrderProductSerializer

    def get_object(self, uid):
        try:
            return OrderProduct.objects.filter(product__store__owner__id=uid,order__order_cancel=False)
        except OrderProduct.DoesNotExist:
            raise Http404

    def get(self, request):
        orders = self.get_object(request.user.id)
        if request.user.is_superuser or request.user.role == 2 or request.user.role == 3 :
            serializer = OrderProductSerializer(orders,many=True)
            return Response({"data": serializer.data,"sucess": True})
        return Response({"message": "You don't permission", "success": False})


class GetStore(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_objects(self,uid):
        try:
            return Store.objects.filter(owner__id=uid)
        except Store.DoesNotExist:
            return Http404

    def get(self,request):
        stores=self.get_objects(request.user.id)
        serializer = StoreSerializer(stores,many=True)
        return Response({"data": serializer.data,"sucess": True})

from product.serializers import GetCatgoriesSerializer


class CategoriesGet(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GetCatgoriesSerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = GetCatgoriesSerializer(category)
        return Response({"data": serializer.data, "success": True})


class AddCategories(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProductCategorySerializer

    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return False

    def post(self, request):
        product = self.get_object(int(request.data['product']))
        if request.user.is_superuser or request.user.role == 2 or product.store.owner.id == request.user.id:
            serializer = ProductCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "status": status.HTTP_201_CREATED, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permission", "success": False})


class ProductCategoriesview(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductCategorySerializer

    def get_object(self, pid):
        try:
            return ProductCategory.objects.filter(product__id=pid)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pid):
        category = self.get_object(pid)
        serializer = GetProductCategoriesSerializer(category,many=True)
        return Response({"data": serializer.data, "success": True})





class CategoriesUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductCategorySerializer

    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = ProductCategorySerializer1(category)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        if request.user.is_superuser or request.user.role == 2 or category.product.store.owner.id==request.user.id:
            
            serializer = ProductCategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, "status": status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions", "success": False})




class ProductStoreWiseView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_object(self, sid):
        try:
            return Product.objects.filter(store__id=sid)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, sid):
        product = self.get_object(sid)
        serializer = ProductSerializer(product,many=True)
        return Response({"data": serializer.data, "success": True})
