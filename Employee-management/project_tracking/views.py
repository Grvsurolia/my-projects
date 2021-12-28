from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Project,OccupiedEmp,BenchList,POCList,PocWorkEmployees
from .serializers import ProjectSerializers,OccupiedEmployeeSerializers,BenchEmployeeSerializers,PocProjectSerializers,PocProjectWorkerSerializers
from employees.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class AddProject(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProjectSerializers

    def post(self, request, *args, **kwargs):
        if request.user.is_bde or request.user.is_ceo or request.user.is_cto or (not(request.user.is_delete)):
            serializer = ProjectSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                project = Project.objects.get(name=serializer.data['name'])
                for emp in serializer.data['assign']:
                    user = User.objects.get(pk=emp)
                    OccupiedEmp.objects.create(
                        project_name=project, emp_name=user, is_active=True)
                    if not (BenchList.objects.all() == []):
                        bench_lists = BenchList.objects.all()
                        for bench_list in bench_lists:
                            if user.id == bench_list.name.id:
                                bench_list.delete()
                return Response({"data": serializer.data, "success": True})
            return Response({"message": serializer.errors, "success": False})
        return Response({"message": "you do not have permission to perform this action.", "success": False})

    def get(self, request):
        project = Project.objects.filter(is_active=True)
        if project == []:
            return Response({"message": "There are no project available"})
        serializer = ProjectSerializers(project, many=True)
        return Response({"data": serializer.data, "success": True})

class ViewAllProject(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProjectSerializers

    def get(self,request,*args,**kwargs):
        project = Project.objects.all()
        if project == []:
            return Response({"message": "There are no project available"})
        serializer = ProjectSerializers(project, many=True)
        return Response({"data": serializer.data, "success": True})
    

class UpdateProject(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProjectSerializers

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ProjectSerializers(queryset)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        if request.user.is_bde or request.user.is_ceo or request.user.is_cto or request.user.is_teamlead or not(request.user.is_delete):
            serializer = ProjectSerializers(queryset, data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                project = Project.objects.get(name=serializer.data['name'])
                for emp in serializer.data['assign']:
                    user = User.objects.get(pk=emp)
                    if not (OccupiedEmp.objects.filter(project_name=project,emp_name=user,is_active=True).exists()):
                        OccupiedEmp.objects.create(project_name=project,emp_name=user,is_active=True)
                        if not (BenchList.objects.all() ==[]):
                            bench_lists =BenchList.objects.all()
                            for bench_list in bench_lists:
                                if user.id==bench_list.name.id:
                                    bench_list.delete() 
                occiuped = OccupiedEmp.objects.filter(project_name=project,is_active=True)  
                for  employee in occiuped:
                    if employee.emp_name.id in serializer.data['assign']:
                        pass
                    else:
                        employee.is_active = False
                        employee.save()
                        BenchList.objects.create(name=employee.emp_name)
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you do not have permission to perform this action.", "success": False})

class AddPocProject(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PocProjectSerializers

    def post(self, request, *args, **kwargs):
        if request.user.is_ceo or request.user.is_cto:
            serializer = PocProjectSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data['project_name'])
                poc_list = POCList.objects.get(project_name=serializer.data['project_name'])
                for emp in serializer.data['assign']:
                    user = User.objects.get(pk=emp)
                    PocWorkEmployees.objects.create(
                        project_name=poc_list, emp_name=user, is_active=True)
                    if not (BenchList.objects.all() == []):
                        bench_lists = BenchList.objects.all()
                        for bench_list in bench_lists:
                            if user.id == bench_list.id:
                                bench_list.delete()
                return Response({"data": serializer.data, "success": True})
            return Response({"message": serializer.errors, "success": False})
        return Response({"message": "you do not have permission to perform this action.", "success": False})

    def get(self, request):
        poc_list = POCList.objects.filter(is_active=True)
        if poc_list == []:
            return Response({"message": "There are no poc_list available"})
        serializer = PocProjectSerializers(poc_list, many=True)
        return Response({"data": serializer.data, "success": True})


class ViewAllPocProject(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PocProjectSerializers

    def get(self,request,*args,**kwargs):
        poclist = POCList.objects.all()
        if poclist == []:
            return Response({"message": "There are no project available"})
        serializer = PocProjectSerializers(poclist, many=True)
        return Response({"data": serializer.data, "success": True})

class UpdatePOCProject(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PocProjectSerializers

    def get_object(self, pk):

        try:
            return POCList.objects.get(pk=pk, is_active=True)
        except POCList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = PocProjectSerializers(queryset)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk):
        queryset = self.get_object(pk)
        if request.user.is_ceo or request.user.is_cto or request.user.is_teamlead or not(request.user.is_delete):
            serializer = PocProjectSerializers(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                poc_list = POCList.objects.get(project_name=serializer.data['project_name'])
                for emp in serializer.data['assign']:
                    user = User.objects.get(pk=emp)
                    if not (PocWorkEmployees.objects.filter(project_name=poc_list, emp_name=user, is_active=True).exists()):
                        PocWorkEmployees.objects.create(
                            project_name=poc_list, emp_name=user, is_active=True)
                        if not (BenchList.objects.all() == []):
                            bench_lists = BenchList.objects.all()
                            for bench_list in bench_lists:
                                if user.id == bench_list.id:
                                    bench_list.delete()
                poc_work_employee = PocWorkEmployees.objects.filter(
                    project_name=poc_list, is_active=True)
                for employee in poc_work_employee:
                    if employee.emp_name.id in serializer.data['assign']:
                        pass
                    else:
                        employee.is_active = False
                        employee.save()
                        BenchList.objects.create(name=employee.emp_name)
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you do not have permission to perform this action.", "success": False})


class AllCurrentlyOccupiedEmployee(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OccupiedEmployeeSerializers

    def get(self, request):
        queryset = OccupiedEmp.objects.filter(is_active=True)
        if queryset == []:
            return Response({"message": "There are no Occupied available", "success": True})
        serializer = OccupiedEmployeeSerializers(queryset, many=True)
        return Response({"data": serializer.data, "success": True})

class ActivePocProjectEmployee(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PocProjectWorkerSerializers

    def get(self, request):
        queryset = PocWorkEmployees.objects.filter(is_active=True)
        if queryset == []:
            return Response({"message": "There are no Occupied available", "success": True})
        serializer = PocProjectWorkerSerializers(queryset, many=True)
        return Response({"data": serializer.data, "success": True})


class AllPocProjectingEmployees(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PocProjectWorkerSerializers

    def get(self, request):
        queryset = PocWorkEmployees.objects.all()
        if queryset == []:
            return Response({"message": "There are no Occupied available", "success": True})
        serializer = PocProjectWorkerSerializers(queryset, many=True)
        return Response({"data": serializer.data, "success": True})



class AllProjectWorkingEmployee(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OccupiedEmployeeSerializers

    def get(self, request):
        queryset = OccupiedEmp.objects.all()
        if queryset == []:
            return Response({"message": "There are no Occupied available"})
        serializer = OccupiedEmployeeSerializers(queryset, many=True)
        return Response({"data": serializer.data, "success": True})


class UpdateOccupiedListEmployee(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OccupiedEmployeeSerializers

    def get_object(self, pk):
        try:
            return OccupiedEmp.objects.get(pk=pk, is_active=True)
        except OccupiedEmp.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = OccupiedEmployeeSerializers(queryset)
        return Response({"data": serializer.data, "success": True})

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if request.user.is_ceo or request.user.is_cto or request.user.is_teamlead:
            serializer = OccupiedEmployeeSerializers(
                queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data, "success": True})
            return Response({"error": serializer.errors, status: status.HTTP_400_BAD_REQUEST, "success": False})
        return Response({"message": "you don't have permissions for update Profile", "success": False})

class AllBenchEmployee(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BenchEmployeeSerializers

    def get(self, request):
        queryset = BenchList.objects.all()
        if queryset == []:
            return Response({"message": " All Employees Task available "})
        serializer = BenchEmployeeSerializers(queryset, many=True)
        return Response({"data": serializer.data, "success": True})



