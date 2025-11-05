"""
Views for Dolfidoc API.
Migrated and adapted from original views.py with REST API architecture.
"""

from collections import defaultdict
from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from .models import Cardiologista, Medicos, Config, Cliente
from .serializers import (
    CardiologistaSerializer,
    CardiologistaFotoSerializer,
    MedicosSerializer,
    ConfigSerializer,
    ClienteSerializer
)


class CardiologistaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listagem e busca de cardiologistas.
    
    GET /api/v1/cardiologistas/ - Lista todos os cardiologistas (paginado)
    GET /api/v1/cardiologistas/?nome_completo=X&especialidade=Y&cidade=Z - Busca filtrada
    GET /api/v1/cardiologistas/<id>/ - Detalhes de um cardiologista
    GET /api/v1/cardiologistas/<id>/foto/ - Retorna a foto do cardiologista
    """
    queryset = Cardiologista.objects.all()
    serializer_class = CardiologistaSerializer
    permission_classes = [AllowAny]  # Para teste — pode voltar a IsAuthenticatedOrReadOnly depois

    def list(self, request, *args, **kwargs):
        # === Parâmetros recebidos ===
        nome_completo = request.GET.get('nome_completo', '').strip()
        especialidade = request.GET.get('especialidade', '').strip()
        cidade = request.GET.get('cidade', '').strip()

        # === Filtros dinâmicos (aplicados antes da paginação) ===
        filtros = Q(valor__gte=1)
        if nome_completo:
            filtros &= Q(nome__icontains=nome_completo)
        if especialidade:
            filtros &= Q(especialidade__icontains=especialidade)
        if cidade:
            filtros &= Q(cidade__icontains=cidade)

        queryset = self.get_queryset().filter(filtros).order_by('valor')

        # === Comportamento inteligente da paginação ===
        # Se o usuário digitou nome_completo, retorna tudo (sem paginação)
        if nome_completo:
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'especialidade': especialidade,
                'cidade': cidade,
                'medicos': serializer.data,
                'total_results': queryset.count(),
                'paginado': False,
            })

        # Caso contrário, aplica paginação padrão
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page if page is not None else queryset, many=True)

        response_data = {
            'especialidade': especialidade,
            'cidade': cidade,
            'medicos': serializer.data,
            'total_results': queryset.count(),
            'paginado': page is not None,
        }

        if page is not None:
            return self.get_paginated_response(response_data)
        return Response(response_data)

    @action(detail=True, methods=['get'])
    def foto(self, request, pk=None):
        """
        Retorna a foto do cardiologista.
        GET /api/v1/cardiologistas/<id>/foto/
        """
        cardiologista = self.get_object()

        if cardiologista.foto:
            return HttpResponse(cardiologista.foto, content_type='image/png')

        return Response(
            {'detail': 'Foto não encontrada.'},
            status=status.HTTP_404_NOT_FOUND
        )
class MedicosViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listagem e busca de médicos.
    
    GET /api/v1/medicos/ - Lista todos os médicos
    GET /api/v1/medicos/?nome=X&especialidade=Y&cidade=Z - Busca filtrada
    GET /api/v1/medicos/<id>/ - Detalhes de um médico
    """
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        """
        Filtra médicos por parâmetros de busca.
        """
        queryset = super().get_queryset()
        
        nome = self.request.GET.get('nome', '').strip()
        especialidade = self.request.GET.get('especialidade', '').strip()
        cidade = self.request.GET.get('cidade', '').strip()
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if especialidade:
            queryset = queryset.filter(especialidade__iexact=especialidade)
        if cidade:
            queryset = queryset.filter(cidade__iexact=cidade)
        
        return queryset.order_by('valor')


class ConfigViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para configurações do sistema.
    
    GET /api/v1/config/ - Lista todas as configurações
    GET /api/v1/config/<id>/ - Detalhes de uma configuração
    """
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD completo de clientes.
    
    GET /api/v1/clientes/ - Lista todos os clientes
    POST /api/v1/clientes/ - Cria um novo cliente
    GET /api/v1/clientes/<id>/ - Detalhes de um cliente
    PUT /api/v1/clientes/<id>/ - Atualiza um cliente
    PATCH /api/v1/clientes/<id>/ - Atualiza parcialmente um cliente
    DELETE /api/v1/clientes/<id>/ - Remove um cliente
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def healthcheck(request):
    """
    Endpoint de healthcheck.
    GET /api/v1/healthcheck/
    """
    return Response({'status': 'ok'})
