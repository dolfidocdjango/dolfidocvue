"""
URL configuration for Dolfidoc API.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CardiologistaViewSet,
    MedicosViewSet,
    ConfigViewSet,
    healthcheck
)

# ============================================================
# ROUTER — registra todas as rotas REST automaticamente
# ============================================================
router = DefaultRouter()
router.register(
    r'cardiologistas',
    CardiologistaViewSet,
    basename='cardiologista'
)

router.register(
    r'medicos',
    MedicosViewSet,
    basename='medico'
)

router.register(
    r'config',
    ConfigViewSet,
    basename='config'
)

# ============================================================
# URL patterns
# ============================================================
urlpatterns = [
    path('', include(router.urls)),

    # Healthcheck
    path('healthcheck/', healthcheck, name='healthcheck'),
]
