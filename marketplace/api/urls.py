from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.viewsets import ProductViewSet, FarmerProfileDetailView, FarmerProfileListCreateView, PackagesView, PackageAcceptView, PackagePackView

router = SimpleRouter()
router.register(r'farmer/products', ProductViewSet, basename='product')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('all-profiles', FarmerProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>', FarmerProfileDetailView.as_view(), name="profile"),
    path('farmer/packages', PackagesView.as_view(), name="orders"),
    path('farmer/packages/accept/<int:pk>', PackageAcceptView.as_view(), name="order_accept"),
    path('farmer/packages/pack/<int:pk>', PackagePackView.as_view(), name="order_pack"),
]