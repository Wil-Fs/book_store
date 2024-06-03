from django.urls import path, include
from rest_framework import routers

from product.viewsets import ProductViewSet
from product.viewsets.category_viewset import CatergoryViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CatergoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]