from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, CompanyViewSet, SupplierViewSet,
    WarehouseViewSet, ProductViewSet
)


router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"companies", CompanyViewSet)
router.register(r"suppliers", SupplierViewSet)
router.register(r"warehouses", WarehouseViewSet)
router.register(r"products", ProductViewSet)


urlpatterns = router.urls
