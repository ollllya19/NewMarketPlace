from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.urls import router as product_router
from customer.urls import router as allproducts_router

router = DefaultRouter()
router.registry.extend(product_router.registry)
router.registry.extend(allproducts_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include(router.urls)),
    path('marketplace/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]