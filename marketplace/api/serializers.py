from dataclasses import fields
from rest_framework import serializers
from api.models import Product, Farmer, Package
from customer.models import Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class PackageAcceptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package
        fields = ['is_accepted']
        

class PackagePackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Package
        fields = ['is_packed']


class FarmerSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model=Farmer
        fields='__all__'
        

class PackageSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        order = Order.objects.get(id=instance.order_id)
        return {
            'ready_dttm': instance.ready_datetm,
            'product': order.product.title,
            'amount': order.amount,
            'is_accepted': instance.is_accepted,
            'is_packed': instance.is_packed,
        }
        