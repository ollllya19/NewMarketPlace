from django.urls import path, include
from rest_framework.routers import SimpleRouter

from customer.views import AllProductsViewSet

router = SimpleRouter()
router.register(r'products', AllProductsViewSet, basename='products')

urlpatterns = []