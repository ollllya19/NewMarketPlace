from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serializers import ProductSerializer
from api.services import ProductViewSetService


class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        return ProductViewSetService().execute_get()
