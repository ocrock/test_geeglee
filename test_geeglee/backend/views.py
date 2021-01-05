from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Customer, Licence, Company
from backend.serializers import CustomerSerializer, LicenceSerializer, CompanySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
