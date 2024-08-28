from django.contrib import admin
from django.urls import path
from app.views import listar_tarefas, criar_tarefa

urlpatterns = [
    path('', listar_tarefas, name='rotaTarefas'),
    path('nova/', criar_tarefa, name='rotaNovaTarefa'),
    # path('editar/', editar_tarefa, name='rotaEditarTarefa'),

]
