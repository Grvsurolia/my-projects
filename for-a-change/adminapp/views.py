# -*- coding: utf-8 -*-
"""
@author: gaurav surolia
"""

from django.shortcuts import render
from rest_framework import generics, permissions, status
from fundraiser.models import Fundraiser, CustomUser
from adminapp.models import RequestedUpdateFundraiser
from fundraiser.serializers import FundraiserSerializer, CustomUserSerializer, AdminUpdateRequestFundraiserSerializer
from donor.models import DonorTransaction
from donor.serializers import DonorTransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.http import HttpResponse, Http404
from django.db.models import Q






#Get All Beneficiaries
class GetAllBeneficiaries(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        # print("permisssssssssss ", request.user, request.user.get_group_permissions(), 'fundraiser.view_fundraiser' in request.user.get_group_permissions())
        # print("grouppppppppppppp ",Group.objects.get(name="admin").user_set.filter(id=request.user.id).exists())
        if 'fundraiser.view_fundraiser' in request.user.get_group_permissions():
            params = list(dict(request.GET).keys())
            if 'search' in params:
                toSearch = request.GET['search']
                fr = Fundraiser.objects.filter(Q(cause__contains=toSearch) | Q(title__contains=toSearch) | Q(slug__contains=toSearch) | Q(beneficiaryFullName__contains=toSearch))
            else:
                fr = Fundraiser.objects.all()
            serializer = FundraiserSerializer(fr, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})


#Delete A Beneficiaries
class DeleteABeneficiaries(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, pk):
        try:
            return Fundraiser.objects.get(pk=pk)
        except Fundraiser.DoesNotExist:
            return status.HTTP_404_NOT_FOUND
    def delete(self, request, pk, format=None):
        if 'fundraiser.delete_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            if fr != 404:
                fr.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"message":"Has No Permission"})


#Delete Multiple Beneficiaries
class DeleteMultipleBeneficiaries(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, request):
        try:
            return Fundraiser.objects.filter(pk__in=request.data['fr_ids'])
        except Fundraiser.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def delete(self, request, format=None):
        if 'fundraiser.delete_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(request)
            if fr.count() != 0:
                fr.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"message":"Has No Permission"})


#Update any Beneficiaries
class UpdateABeneficiarie(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return Fundraiser.objects.get(pk=pk)
        except Fundraiser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if 'fundraiser.view_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            serializer = FundraiserSerializer(fr)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})

    def put(self, request, pk, format=None):
        if 'fundraiser.change_fundraiser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            serializer = FundraiserSerializer(fr, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Has No Permission"})


#Get All Campaigners
class GetAllCampaigners(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        if 'fundraiser.view_customuser' in request.user.get_group_permissions():
            params = list(dict(request.GET).keys())
            if 'search' in params:
                toSearch = request.GET['search']
                users = CustomUser.objects.filter(Q(full_name__contains=toSearch) | Q(email__contains=toSearch) | Q(phone_number__contains=toSearch))
            else:
                users = CustomUser.objects.exclude(id=request.user.id)
            serializer = CustomUserSerializer(users, many=True)
            for usr in serializer.data:
                frCount = Fundraiser.objects.filter(user=usr["id"]).count()
                usr["frCount"] = frCount
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})


#Delete A Campainer
class DeleteACampaigner(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return status.HTTP_404_NOT_FOUND
    def delete(self, request, pk, format=None):
        if 'fundraiser.delete_customuser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            if fr != 404:
                fr.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"Has No Permission"})


#Delete Multiple Campaigners
class DeleteMultipleCampaigners(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, request):
        try:
            return CustomUser.objects.filter(pk__in=request.data['campaignerids'])
        except CustomUser.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def delete(self, request, format=None):
        if 'fundraiser.delete_customuser' in request.user.get_group_permissions():
            fr = self.get_object(request)
            if fr.count() != 0:
                fr.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"message":"Has No Permission"})


#Update any Campaigner
class UpdateACampaigners(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if 'fundraiser.view_customuser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            serializer = CustomUserSerializer(fr)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})

    def put(self, request, pk, format=None):
        if 'fundraiser.change_customuser' in request.user.get_group_permissions():
            fr = self.get_object(pk)
            serializer = CustomUserSerializer(fr, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Has No Permission"})


#Get All Transactions
class GetAllTransactions(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        if 'donor.view_donortransaction' in request.user.get_group_permissions():
            params = list(dict(request.GET).keys())
            if 'search' in params:
                toSearch = request.GET['search']
                donors = DonorTransaction.objects.filter(Q(full_name__contains=toSearch) | Q(email__contains=toSearch) | Q(phone_number__contains=toSearch) | Q(billingCity__contains=toSearch))
            elif 'gt_amount' in params and 'lt_amount' in params:
                gt_amount = request.GET['gt_amount']
                lt_amount = request.GET['lt_amount']
                donors = DonorTransaction.objects.filter(amount__gt=gt_amount, amount__lt=lt_amount)
            elif 'gt_amount' in params:
                toSearch = request.GET['gt_amount']
                donors = DonorTransaction.objects.filter(Q(amount__gt=toSearch))
            elif 'lt_amount' in params:
                toSearch = request.GET['lt_amount']
                donors = DonorTransaction.objects.filter(Q(amount__lt=toSearch))
            else:
                donors = DonorTransaction.objects.all()
            serializer = DonorTransactionSerializer(donors, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})


#Delete A Transaction
class DeleteATransaction(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, pk):
        try:
            return DonorTransaction.objects.get(pk=pk)
        except DonorTransaction.DoesNotExist:
            return status.HTTP_404_NOT_FOUND
    def delete(self, request, pk, format=None):
        if 'donor.delete_donortransaction' in request.user.get_group_permissions():
            donor = self.get_object(pk)
            if donor != 404:
                donor.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"Has No Permission"})


#Delete Multiple Transactions
class DeleteMultipleTransactions(APIView):
    permission_classes = (permissions.IsAdminUser,)
    
    def get_object(self, request):
        try:
            return DonorTransaction.objects.filter(pk__in=request.data['transids'])
        except CustomUser.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def delete(self, request, format=None):
        if 'donor.delete_donortransaction' in request.user.get_group_permissions():
            donor = self.get_object(request)
            if donor.count() != 0:
                donor.delete()
                return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message":"Wrong Id or Id not Found"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response({"message":"Has No Permission"})


#Update any Transaction
class UpdateATransaction(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get_object(self, pk):
        try:
            return DonorTransaction.objects.get(pk=pk)
        except DonorTransaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if 'fundraiser.view_customuser' in request.user.get_group_permissions():
            trans = self.get_object(pk)
            serializer = DonorTransactionSerializer(trans)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})

    def put(self, request, pk, format=None):
        if 'fundraiser.change_customuser' in request.user.get_group_permissions():
            trans = self.get_object(pk)
            serializer = DonorTransactionSerializer(trans, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Has No Permission"})


#Create Campaigner
class CreateCampaigner(generics.CreateAPIView):

    permission_classes = (permissions.IsAdminUser,)    
        
    def post(self, request, format=None):
        if request.user.is_active:
            if 'fundraiser.add_customuser' in request.user.get_group_permissions():
                request.data._mutable = True
                request.data["username"] = request.data["email"].split("@")[0]
                campaignerGroupId = Group.objects.get(name="campaigner")
                request.data["groups"] = campaignerGroupId.id
                # request.data["is_active"] = True
                request.data._mutable = False
                serializer = CustomUserSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message':"Has No Permissions",'status':status.HTTP_200_OK})
        return Response({'message':"please Activate/Verify Your account",'status':status.HTTP_200_OK})


#Get All Active Beneficiary Request
class GetAllActiveBeneficiaryRequest(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        if 'fundraiser.view_requestupdatefundraiser' in request.user.get_group_permissions():
            frRequest = RequestedUpdateFundraiser.objects.all()
            serializer = AdminUpdateRequestFundraiserSerializer(frRequest, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"Has No Permission"})