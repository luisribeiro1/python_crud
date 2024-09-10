from rest_framework import serializers
from .models import Tarefa, Usuario 

#Serialzar é converto os obejetos dos modeledos em JSON e vice-versa

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome']

class TarefaSerializer(serializers.ModelSerializer):

    #responsavel = serializers.StringRelatedField()
    responsavel_nome = serializers.CharField(source='responsavel.nome', read_only=True)
    
    class Meta:
        model = Tarefa
        fields = ['id_tarefa','titulo','responsavel','responsavel_nome','prazo','status']


