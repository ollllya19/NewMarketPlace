from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.urls import router as product_router

router = DefaultRouter()
router.registry.extend(product_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include(router.urls)),
]