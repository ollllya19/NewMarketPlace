from rest_framework.routers import SimpleRouter

from customer.views import AllProductsViewSet, CartsViewSet

router = SimpleRouter()
router.register(r'products', AllProductsViewSet, basename='products')
router.register(r'cart', CartsViewSet, basename='cart')


urlpatterns = []