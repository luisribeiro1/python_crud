from django.urls import path
from .views import listar_tarefas

urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    # path('edit/<int:id>', edit_item, name='edit_item'),
]
