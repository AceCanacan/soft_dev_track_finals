from django.urls import include, path
from products.views import ProductViewSet, ProductImageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]