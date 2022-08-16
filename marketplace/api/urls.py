from rest_framework.routers import SimpleRouter

from api.viewsets import ProductViewSet


router = SimpleRouter()
router.register(r'farmer', ProductViewSet, basename='product')

urlpatterns = []