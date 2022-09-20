from rest_framework import serializers
from api.models import Product
from .models import Cart


class AllProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['product', 'col']


class CartCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Cart
        fields = '__all__'