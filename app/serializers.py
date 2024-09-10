from rest_framework import serializers
from .models import Tarefa, Usuario

# Serializar é converter os objetos dos modelos em JSON E vice-versa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id.usuario', 'nome']

class TarefaSerializer(serializers.ModelSerializer):
    
    #responsavel = serializers.StringRelatedField()
    
    responsavel_nome = serializers.CharField(source='responsavel.nome', read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id_tarefa', 'titulo', 'prazo', 'responsavel', 'responsavel_nome', 'status']