from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'html/listar_tarefas.html', {'lista_tarefas': tarefas})

def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaTarefas')

    else: 
        form = TarefaForm()

    return render(request, 'html/form_tarefa.html', {'form': form})
    