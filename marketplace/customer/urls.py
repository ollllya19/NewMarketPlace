from rest_framework.routers import SimpleRouter

from customer.views import AllProductsViewSet, CartsViewSet, OrderViewSet

router = SimpleRouter()
router.register(r'products', AllProductsViewSet, basename='products')
router.register(r'cart', CartsViewSet, basename='cart')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = []
