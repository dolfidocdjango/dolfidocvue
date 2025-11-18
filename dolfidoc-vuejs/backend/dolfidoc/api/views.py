"""
Views for Dolfidoc API — versão otimizada e ajustada à nova modelagem.
"""

from django.db.models import Q, F, Value
from django.db.models.functions import Concat
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.http import HttpResponse

from .models import (
    Cardiologista,
    Medicos,
    Endereco,
    Clinica,
    CBO
)

from .serializers import (
    CardiologistaSerializer,
    CardiologistaFotoSerializer,
    MedicosSerializer,
    ConfigSerializer,
)
from .models import Config


# ============================================================
# 1) CARDIOLOGISTA — permanece igual
# ============================================================
class CardiologistaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cardiologista.objects.all()
    serializer_class = CardiologistaSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        nome_completo = request.GET.get('nome_completo', '').strip()
        especialidade = request.GET.get('especialidade', '').strip()
        cidade        = request.GET.get('cidade', '').strip()

        filtros = Q(valor__gte=1)

        if nome_completo:
            filtros &= Q(nome__icontains=nome_completo)
        if especialidade:
            filtros &= Q(especialidade__icontains=especialidade)
        if cidade:
            filtros &= Q(cidade__icontains=cidade)

        queryset = self.get_queryset().filter(filtros).order_by('valor')

        if nome_completo:
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'especialidade': especialidade,
                'cidade': cidade,
                'medicos': serializer.data,
                'total_results': queryset.count(),
                'paginado': False,
            })

        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page if page else queryset, many=True)

        response_data = {
            'especialidade': especialidade,
            'cidade': cidade,
            'medicos': serializer.data,
            'total_results': queryset.count(),
            'paginado': page is not None,
        }

        if page:
            return self.get_paginated_response(response_data)

        return Response(response_data)

    @action(detail=True, methods=['get'])
    def foto(self, request, pk=None):
        cardiologista = self.get_object()
        if cardiologista.foto:
            return HttpResponse(cardiologista.foto, content_type='image/png')
        return Response({'detail': 'Foto não encontrada.'}, status=404)


class MedicosViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para listagem e busca de médicos, seguindo a MESMA lógica do CardiologistaViewSet.
    
    GET /api/v1/medicos/
    GET /api/v1/medicos/?nome_completo=X&especialidade=Y&cidade=Z
    GET /api/v1/medicos/<id>/
    """
    
    queryset = Medicos.objects.select_related(
        "cod_cbo",
        "clinica",
        "clinica__endereco"
    )
    serializer_class = MedicosSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):

        # === Parâmetros ===
        nome_completo = request.GET.get('nome_completo', '').strip()
        especialidade = request.GET.get('especialidade', '').strip()
        cidade        = request.GET.get('cidade', '').strip()
        uf            = request.GET.get('uf', '').strip()
        cbo_code      = request.GET.get('cbo', '').strip()

        # === BASE DO FILTRO ===
        filtros = Q(id__gte=1)

        # nome do médico
        if nome_completo:
            filtros &= Q(no_profissional__icontains=nome_completo)

        # especialidade via tabela CBOEspecialidade
        if especialidade:
            filtros &= Q(
                cod_cbo__especialidades__cod_cbo_especialidades_label__icontains=especialidade
            )

        # código CBO
        if cbo_code:
            filtros &= Q(cod_cbo__cod_cbo__icontains=cbo_code)

        # cidade da clínica
        if cidade:
            filtros &= Q(clinica__endereco__no_municipio__icontains=cidade)

        # uf (estado) da clínica
        if uf:
            filtros &= Q(clinica__endereco__co_sigla_estado__iexact=uf)

        queryset = self.get_queryset().filter(filtros).order_by("no_profissional")

        # === Comportamento inteligente da paginação (mesma lógica do cardiologista) ===
        if nome_completo:
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "especialidade": especialidade,
                "cidade": cidade,
                "uf": uf,
                "cbo": cbo_code,
                "medicos": serializer.data,
                "total_results": queryset.count(),
                "paginado": False,
            })

        # Paginação padrão
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page if page else queryset, many=True)

        response_data = {
            "especialidade": especialidade,
            "cidade": cidade,
            "uf": uf,
            "cbo": cbo_code,
            "medicos": serializer.data,
            "total_results": queryset.count(),
            "paginado": page is not None,
        }

        if page:
            return self.get_paginated_response(response_data)
        return Response(response_data)



# ============================================================
# 3) CONFIG
# ============================================================
class ConfigViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    permission_classes = [AllowAny]


# ============================================================
# 4) HEALTHCHECK
# ============================================================
@api_view(["GET"])
def healthcheck(request):
    return Response({"status": "ok"})
