from rest_framework import serializers
from api.models import Product
from .models import Cart


class AllProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
        

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['product', 'col']
        depth = 1
