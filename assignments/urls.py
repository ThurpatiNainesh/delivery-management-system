from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, AgentViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'agents', AgentViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]