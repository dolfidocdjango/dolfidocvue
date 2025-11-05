"""
Tests for Dolfidoc API.
"""

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Cliente


class ClienteAPITestCase(APITestCase):
    """
    Testes para o endpoint de clientes.
    """
    
    def setUp(self):
        """Configuração inicial para os testes."""
        self.cliente_data = {
            'nome': 'João Silva',
            'email': 'joao@example.com',
            'telefone': '11999999999',
            'ativo': True
        }
    
    def test_criar_cliente(self):
        """Testa a criação de um cliente."""
        response = self.client.post('/api/v1/clientes/', self.cliente_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nome, 'João Silva')
    
    def test_listar_clientes(self):
        """Testa a listagem de clientes."""
        Cliente.objects.create(**self.cliente_data)
        response = self.client.get('/api/v1/clientes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class HealthcheckTestCase(APITestCase):
    """
    Testes para o endpoint de healthcheck.
    """
    
    def test_healthcheck(self):
        """Testa o endpoint de healthcheck."""
        response = self.client.get('/api/v1/healthcheck/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'ok'})
