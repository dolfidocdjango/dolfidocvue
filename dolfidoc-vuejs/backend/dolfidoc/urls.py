"""
URL configuration for dolfidoc project.
"""

from django.contrib                 import admin
from django.urls                    import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # ============================================================
    # ADMIN
    # ============================================================
    path('admin/', admin.site.urls),


    # ============================================================
    # AUTH — JWT Tokens
    # ============================================================
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # ============================================================
    # API v1 — CORE
    # ============================================================
    path('api/v1/', include('dolfidoc.api.urls')),


    # ============================================================
    # API v1 — Usuarios
    # ============================================================
    path('api/v1/users/', include('dolfidoc.users.urls')),
]
