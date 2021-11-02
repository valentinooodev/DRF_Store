from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, ProductTagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)


app_name = 'store_api'

urlpatterns = [
    path('', include(router.urls)),
]