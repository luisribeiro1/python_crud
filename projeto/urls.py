from django.contrib import admin
from django.urls import path
from app.views import listar_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa
from app.usuario_views import listar_usuarios, criar_usuario, editar_usuario, excluir_usuario

urlpatterns = [
    path('', listar_tarefas, name='rotaTarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    path('editar/<int:id>/', editar_tarefa, name='rotaEditarTarefa'),
    path('excluir/<int:id>/', excluir_tarefa, name='rotaExcluirTarefa'),

    path('usuarios/', listar_usuarios, name='rotaUsuarios'),
    path('usuarios/nova/', criar_usuario, name='rotaNovoUsuario'),
    path('usuarios/editar/<int:id>/', editar_usuario, name='rotaEditarUsuario'),
    path('usuarios/excluir/<int:id>/', excluir_usuario, name='rotaExcluirUsuario'),
]
