from rest_framework import serializers
from api.models import Product


class AllProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
