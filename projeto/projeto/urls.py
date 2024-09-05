from django.contrib import admin
from django.urls import path
from app.views import listar_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa
from app.views_usuario import listar_usuarios, criar_usuario, editar_usuario, excluir_usuario

urlpatterns = [
    path('', listar_tarefas, name='rotaTarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    path('editar/<int:id>/', editar_tarefa, name='rotaEditarTarefa'),
    path('excluir/<int:id>/', excluir_tarefa, name='rotaExcluirTarefa'),

    path('usuario/', listar_usuarios, name='rotaUsuarios'),
    path('usuario/nova/', criar_usuario, name='rotaNovaUsuario'),
    path('usuario/editar/<int:id>/', editar_usuario, name='rotaEditarUsuario'),
    path('usuario/excluir/<int:id>/', excluir_usuario, name='rotaExcluirUsuario'),
]
