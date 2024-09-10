from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tarefa, Usuario
from .serializers import TarefaSerializer, UsuarioSerializer

@api_view(['GET', 'POST'])      # Decorator que indica quais metodos a view aceita
def tarefas_api(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()      # Objeto de model
        serializer = TarefaSerializer(tarefas, many=True)       # Converter um objeto em JSON
        return Response(serializer.data)        # Responder com o conteudo em JSON
    
    elif request.method == "POST":
        serializer = TarefaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"resultado":"OK"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tarefas_detalhes_api(request, id):
    try:
        tarefa = Tarefa.objects.get(pk=id)
    except Tarefa.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request == 'GET':
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
