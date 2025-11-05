"""
Admin configuration for API models.
"""

from django.contrib import admin
from .models import Cardiologista, Medicos, Config, Cliente


@admin.register(Cardiologista)
class CardiologistaAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Cardiologista.
    """
    list_display = ['nome', 'crm', 'uf', 'cidade', 'especialidade', 'valor']
    list_filter = ['uf', 'cidade', 'especialidade']
    search_fields = ['nome', 'crm', 'cidade', 'especialidade']
    ordering = ['valor', 'nome']
    list_per_page = 50


@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Medicos.
    """
    list_display = ['nome', 'crm', 'uf', 'cidade', 'especialidade', 'situacao', 'valor']
    list_filter = ['uf', 'cidade', 'especialidade', 'situacao']
    search_fields = ['nome', 'crm', 'cidade', 'especialidade']
    ordering = ['valor', 'nome']
    list_per_page = 50


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Config.
    """
    list_display = ['name', 'email', 'feedback']
    search_fields = ['name', 'email']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuração do admin para Cliente.
    """
    list_display = ['nome', 'email', 'telefone', 'ativo', 'data_criacao']
    list_filter = ['ativo', 'data_criacao']
    search_fields = ['nome', 'email', 'telefone']
    ordering = ['-data_criacao']
    list_per_page = 50
