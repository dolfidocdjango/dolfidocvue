"""
Views for User management.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserCreateSerializer, UserProfileSerializer
from .permissions import IsAdminOrOwner

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de usuários.
    
    GET /api/v1/users/ - Lista todos os usuários (somente admin)
    POST /api/v1/users/ - Cria um novo usuário
    GET /api/v1/users/<id>/ - Detalhes de um usuário
    PUT /api/v1/users/<id>/ - Atualiza um usuário
    PATCH /api/v1/users/<id>/ - Atualiza parcialmente um usuário
    DELETE /api/v1/users/<id>/ - Remove um usuário (somente admin)
    GET /api/v1/users/profile/ - Retorna o perfil do usuário autenticado
    """
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        """Retorna o serializer apropriado baseado na ação."""
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'profile':
            return UserProfileSerializer
        return UserSerializer
    
    def get_permissions(self):
        """Define permissões baseadas na ação."""
        if self.action == 'create':
            # Qualquer um pode criar uma conta
            return []
        elif self.action == 'destroy':
            # Somente admins podem deletar usuários
            return [IsAdminUser()]
        elif self.action in ['update', 'partial_update']:
            # Admin ou próprio usuário pode atualizar
            return [IsAdminOrOwner()]
        elif self.action == 'profile':
            # Somente usuários autenticados podem ver seu próprio perfil
            return [IsAuthenticated()]
        else:
            # Outras ações requerem autenticação
            return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def profile(self, request):
        """
        Retorna o perfil do usuário autenticado.
        GET /api/v1/users/profile/
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
