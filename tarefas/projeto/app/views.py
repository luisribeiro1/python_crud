from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefas
from .forms import TarefaForm

# Criar uma função para listar as tarefas
def listar_tarefas(request):
#    lista_de_tarefas = Tarefas.objects.all()
    lista_de_tarefas = Tarefas.objects.order_by('id_tarefa')

    return render(request, 'app_html/lista_tarefas.html', {'lista_tarefas': lista_de_tarefas})

def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaTarefas')


    else:
        form = TarefaForm()


    return render(request, 'app_html/form_tarefas.html', {'form': form})


# Esta view recebe o parâmetro 'id' que foi definido na rota.
def editar_tarefa(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro 'id'
    tarefa = get_object_or_404(Tarefas, id_tarefa=id)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('rotaTarefas')


    else:
        form = TarefaForm(instance=tarefa)


    return render(request, 'app_html/form_tarefas.html', {'form': form})


def excluir_tarefa(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro 'id'
    tarefa = get_object_or_404(Tarefas, id_tarefa=id)

    if request.method == "POST":
        tarefa.delete()
        return redirect('rotaTarefas')

    return render(request, 'app_html/excluir_tarefa.html', {'tarefa': tarefa})