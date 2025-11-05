"""
Custom permissions for Dolfidoc API.
"""

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada que permite:
    - Leitura para qualquer usuário autenticado
    - Escrita/Deleção apenas para administradores
    """
    
    def has_permission(self, request, view):
        # Permite métodos de leitura (GET, HEAD, OPTIONS) para qualquer usuário autenticado
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Permite métodos de escrita apenas para administradores
        return request.user and request.user.is_authenticated and request.user.is_staff
