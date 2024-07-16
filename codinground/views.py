from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import invoicebillSerializer,invoiceHeaderSerializer,invoiceItemSerializer
from .models import invoiceBill,invoiceHeader,invoiceItem


class viewinvoiceBillSet(viewsets.ModelViewSet):
    queryset  = invoiceBill.objects.all()
    serializer_class = invoicebillSerializer


class viewinvoiceHeaderSet(viewsets.ModelViewSet):
    queryset = invoiceHeader.objects.all()
    serializer_class = invoiceHeaderSerializer

class viewinvoiceItemSet(viewsets.ModelViewSet):
    queryset = invoiceItem.objects.all()
    serializer_class = invoiceItemSerializer


