from django.urls import path
from .views import listar_tarefas, criar_tarefa

urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    #path('editar/', editar_tarefa, name='rotaEditarTarefa'),
]