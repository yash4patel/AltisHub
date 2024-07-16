from rest_framework import serializers
from .models import invoiceBill,invoiceHeader,invoiceItem
# from rest_framework.serializers import ValidationError

class invoicebillSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceBill
        fields = "__all__"
        def validate(self,data):
            if data['amount'] == 0:
                raise serializers.ValidationError("amount can be negative or positive")



class invoiceHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceHeader
        fields = "__all__"

        
    
class invoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoiceItem
        fields = ['id', 'item_name', 'quantity', 'price', 'amount']
        def validate(self, data):
            if data['quantity'] <= 0 or data['price'] <= 0 or data['amount'] <= 0:
                raise serializers.ValidationError("Quantity, Price, and Amount must be greater than zero.")
            return data
       