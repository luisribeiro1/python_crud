from django.shortcuts import render, redirect
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