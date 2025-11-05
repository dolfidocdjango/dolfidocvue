# serializers.py

from rest_framework import serializers
from .models import Cardiologista, Medicos, Config, Cliente


class CardiologistaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Cardiologista.
    """
    cidade_uf = serializers.SerializerMethodField()
    
    # === INÍCIO DA CORREÇÃO ===
    
    # 1. Campo para formatar o preço como o frontend espera
    valores_consulta = serializers.SerializerMethodField()
    
    # 2. Campo para expor a URL da foto de forma segura
    foto_url = serializers.SerializerMethodField()
    
    # === FIM DA CORREÇÃO ===

    class Meta:
        model = Cardiologista
        fields = [
            'id', 'nome', 'crm', 'uf', 'cidade', 'cidade_uf',
            'nome_fantasia', 'cnpj', 'especialidade', 'numero',
            'fid', 'logradouro', 'complemento',
            
            # === INÍCIO DA CORREÇÃO ===
            
            # 3. Substituímos 'valor' pelos novos campos
            'valores_consulta',
            'foto_url'
            
            # === FIM DA CORREÇÃO ===
        ]
    
    def get_cidade_uf(self, obj):
        """Retorna cidade e UF concatenados."""
        if obj.cidade and obj.uf:
            return f"{obj.cidade} - {obj.uf}"
        return None

    # === INÍCIO DA CORREÇÃO ===

    # 4. Método para "fabricar" o array de valores
    def get_valores_consulta(self, obj):
        """
        Transforma o campo 'valor' em um array 'valores_consulta'
        para compatibilidade com o frontend Vue.js.
        """
        if obj.valor is not None:
            # O frontend espera um array [150.00]
            return [obj.valor]
        # Retorna array vazio se não houver preço (seguro para o v-for)
        return []

    # 5. Método para gerar a URL da foto
    def get_foto_url(self, obj):
        """
        Retorna o caminho relativo para a action 'foto' se obj.foto existir.
        """
        if obj.foto:
            # O frontend usará isso para chamar a action 'foto' da viewset
            return f"cardiologistas/{obj.id}/foto/"
        return None
    
    # === FIM DA CORREÇÃO ===


class CardiologistaFotoSerializer(serializers.ModelSerializer):
    """
    Serializer específico para retornar foto do cardiologista.
    """
    class Meta:
        model = Cardiologista
        fields = ['id', 'foto']


class MedicosSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Medicos.
    """
    cidade_uf = serializers.SerializerMethodField()
    
    class Meta:
        model = Medicos
        fields = [
            'id', 'nome', 'crm', 'situacao', 'uf', 'cidade', 'cidade_uf',
            'nome_fantasia', 'cnpj', 'especialidade', 'numero',
            'logradouro', 'complemento', 'valor'
        ]
    
    def get_cidade_uf(self, obj):
        """Retorna cidade e UF concatenados."""
        if obj.cidade and obj.uf:
            return f"{obj.cidade} - {obj.uf}"
        return None


class ConfigSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Config.
    """
    class Meta:
        model = Config
        fields = ['id', 'name', 'email', 'feedback', 'comment']


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Cliente.
    """
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'data_criacao', 'ativo']
        read_only_fields = ['data_criacao']
