from django.contrib import admin
from django.urls import path
from app.views import listar_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa

urlpatterns = [
    path('', listar_tarefas, name='rotaTarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    path('editar/<int:id>/', editar_tarefa, name='rotaEditarTarefa'),
    path('excluir/<int:id>/', excluir_tarefa, name='rotaExcluirTarefa'),
    path('usuarios/', listar_usuarios, name='rotaUsuarios')
]
