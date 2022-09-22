from rest_framework import serializers
from api.models import Product
from .models import Cart, OrderItem

#Products
class AllProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        

#Cart
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['product', 'col']


class CartCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Cart
        fields = '__all__'
        
 
 #Order
class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        exclude = ['order']
    
    
class OrderSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'created_datetime': instance.created_datetime,
            'deliv_date': instance.deliv_date,
            'address': instance.address,
            'product': OrderItemSerializer(OrderItem.objects.filter(order=instance), many=True).data,
        }
        