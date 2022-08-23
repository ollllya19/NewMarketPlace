from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.viewsets import ProductViewSet

router = SimpleRouter()
router.register(r'farmer/products', ProductViewSet, basename='product')

urlpatterns = [

]