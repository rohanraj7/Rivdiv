from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Invoice,InvoiceDetail
from rivapp.api.serializers import InvoiceSerializer,InvoiceDetailSerializer

# Create your views here.

class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.AllowAny]

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    permission_classes = [permissions.AllowAny]


