from django.urls import path
from .views import listar_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa

urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    path('editar/<int:id>/', editar_tarefa, name='rotaEditarTarefa'),
    path('excluir/<int:id>/', excluir_tarefa, name='rotaExcluirTarefa'),
]