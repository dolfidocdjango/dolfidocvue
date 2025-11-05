"""
Custom permissions for User management.
"""

from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Permissão customizada que permite:
    - Administradores podem fazer qualquer coisa
    - Usuários podem editar apenas seu próprio perfil
    """
    
    def has_object_permission(self, request, view, obj):
        # Administradores têm acesso total
        if request.user and request.user.is_staff:
            return True
        
        # Usuários podem editar apenas seu próprio perfil
        return obj == request.user
