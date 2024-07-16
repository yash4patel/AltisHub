from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import viewinvoiceItemSet,viewinvoiceHeaderSet,viewinvoiceBillSet

routes = DefaultRouter()
routes.register(r'invoicebill',viewinvoiceBillSet)
routes.register(r'invoiceheader',viewinvoiceHeaderSet)
routes.register(r'invoiceitem',viewinvoiceItemSet)



urlpatterns = [
    path('',include(routes.urls))
]
