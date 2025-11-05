"""
Custom User model for Dolfidoc.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo de usuário customizado estendendo AbstractUser.
    Permite adicionar campos personalizados conforme necessário.
    """
    
    # Campos adicionais podem ser adicionados aqui
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.username
