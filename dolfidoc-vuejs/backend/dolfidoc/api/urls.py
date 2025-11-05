"""
URL configuration for Dolfidoc API.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CardiologistaViewSet,
    MedicosViewSet,
    ConfigViewSet,
    ClienteViewSet,
    healthcheck
)

# Router para ViewSets
router = DefaultRouter()
router.register(r'cardiologistas', CardiologistaViewSet, basename='cardiologista')
router.register(r'medicos', MedicosViewSet, basename='medico')
router.register(r'config', ConfigViewSet, basename='config')
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls)),
    path('healthcheck/', healthcheck, name='healthcheck'),
]
