"""
Serializers for User management.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para listagem e detalhes de usuários.
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefone', 'data_nascimento', 'is_active', 'is_staff',
            'date_joined', 'last_login'
        ]
        read_only_fields = ['date_joined', 'last_login']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de usuários.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name', 'telefone', 'data_nascimento'
        ]
    
    def validate(self, attrs):
        """Valida se as senhas coincidem."""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        return attrs
    
    def create(self, validated_data):
        """Cria um novo usuário."""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para perfil do usuário autenticado.
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefone', 'data_nascimento', 'is_active', 'is_staff',
            'date_joined', 'last_login'
        ]
        read_only_fields = ['username', 'date_joined', 'last_login', 'is_staff']
