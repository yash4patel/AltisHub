from typing import Iterable
from django.db import models

# Create your models here.

# Invoice Header
# Id: UUID
# Date: string (UTC)
# InvoiceNumber: number
# CustomerName: string
# BillingAddress: string
# ShippingAddress: string
# GSTIN: string
# TotalAmount: Decimal


class invoiceHeader(models.Model):
    UUID = models.IntegerField()
    date = models.DateTimeField()
    invoiceNumber = models.AutoField(primary_key = True)
    CustomerName = models.CharField(max_length = 50)
    billingAddress = models.CharField(max_length = 100)
    shippingAddress = models.CharField(max_length = 100)
    GSTIN = models.CharField(max_length = 100)
    totalAmount = models.FloatField()


# Invoice Items
# Id: UUID
# itemName: string
# Quantity: decimal
# Price: decimal
# Amount: decimal
    

class invoiceItem(models.Model):
    UUID= models.ForeignKey(invoiceHeader,on_delete = models.CASCADE)
    itemName = models.CharField(max_length = 100)
    quantity = models.FloatField()
    price = models.FloatField()
    amount = models.FloatField()
    def save(self,*args, **kwargs):
        self.amount = self.price*self.quantity
        super().save(*args, **kwargs)
    amount = models.FloatField()


# Invoice BillSundry
# Id: UUID
# billSundryName: string
# Amount: decimal


class invoiceBill(models.Model):
    UUID= models.ForeignKey(invoiceHeader,on_delete = models.CASCADE)
    billName = models.CharField(max_length = 100)
    amount = models.FloatField()

