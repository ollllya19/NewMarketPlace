from rest_framework import serializers
from api.models import Product, Farmer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FarmerSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Farmer
        fields='__all__'





# not used yet
class ProductsSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'description': instance.description,
        }
        