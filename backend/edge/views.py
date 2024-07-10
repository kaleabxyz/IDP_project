from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
@api_view(['GET'])
def getData(request):
    return Response()

class Backendviewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Doctor.objects.all()
    serializer_class = BackendSerializer
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        queryset = self.queryset
        serializer =self.serializer_class(queryset, many = True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        doctor = self.queryset.get(pk = pk)
        serializer = self.serializer_class(doctor)
        return Response(serializer.data)
    

    def update(self, request, pk=None):
        doctor = self.queryset.get(pk = pk)
        serializer = self.serializer_class(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    

    def destroy(self, request, pk=None):
        doctor = self.queryset.get(pk = pk)
        doctor.delete()
        return Response(status=204)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PatientSerializer

    def list(self, request):
        queryset = self.queryset
        serializer =self.serializer_class(queryset, many = True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        Patient = self.queryset.get(pk = pk)
        serializer = self.serializer_class(Patient)
        return Response(serializer.data)
    

    def update(self, request, pk=None):
        Patient = self.queryset.get(pk = pk)
        serializer = self.serializer_class(Patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    

    def destroy(self, request, pk=None):
        Patient = self.queryset.get(pk = pk)
        Patient.delete()
        return Response(status=204)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = self.queryset
        serializer =self.serializer_class(queryset, many = True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        room = self.queryset.get(pk = pk)
        serializer = self.serializer_class(room)
        return Response(serializer.data)
    

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    

    def destroy(self, request, pk=None):
        room = self.queryset.get(pk = pk)
        room.delete()
        return Response(status=204)
