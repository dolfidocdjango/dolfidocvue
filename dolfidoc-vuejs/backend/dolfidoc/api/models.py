"""
Models for Dolfidoc API.
Migrated from original dolfidocapp models.
"""

from django.db import models


class Cardiologista(models.Model):
    """
    Modelo para armazenar informações de cardiologistas.
    Migrado da tabela 'cardiologista' do banco original.
    """
    nome = models.CharField(max_length=255, blank=True, null=True)
    crm = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=255, blank=True, null=True)
    especialidade = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fid = models.CharField(max_length=255, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'cardiologista'
        verbose_name = 'Cardiologista'
        verbose_name_plural = 'Cardiologistas'
        ordering = ['valor', 'nome']

    def __str__(self):
        return f"{self.nome} - {self.crm}/{self.uf}"


class Medicos(models.Model):
    """
    Modelo para armazenar informações de médicos.
    Migrado da tabela 'medicos' do banco original.
    """
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=50)
    situacao = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=5)
    cidade = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=150, blank=True, null=True)
    cnpj = models.CharField(max_length=30, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=150, blank=True, null=True)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'medicos'
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['valor', 'nome']

    def __str__(self):
        return f"{self.nome} - {self.crm}/{self.uf}"


class Config(models.Model):
    """
    Modelo para armazenar configurações do sistema.
    Migrado da tabela 'config' do banco original.
    """
    backgroundfoto = models.BinaryField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    feedback = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'config'
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return f"Config: {self.name}"


class Cliente(models.Model):
    """
    Modelo para CRUD de clientes.
    Novo modelo conforme especificação do documento.
    """
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-data_criacao']

    def __str__(self):
        return f"{self.nome} - {self.email}"
