from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    # Obter os dados das farefas
    lista_de_tarefas = Tarefa.objects.all()

    # Renderizar o template
    return render(request, 'app_html/lista_tarefas.html', {'lista_tarefas': lista_de_tarefas})

def criar_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaTarefas')

    else:
        form = TarefaForm()

    return render(request, 'app_html/form_tarefa.html', {'form': form})




