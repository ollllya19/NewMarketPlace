import json
import requests
from rest_framework import status
from rest_framework.response import Response

from api.serializers import ProductsSerializer
from api.repositories import ProductRepository


class ProductViewSetService:
    
    __slots__ = 'request',

    def __init__(self, request=None):
        self.request = request

    def execute_get(self):
        queryset = ProductRepository.get_all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)
    