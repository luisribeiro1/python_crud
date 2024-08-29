from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
  # Caso queira ordenar: lista_tarefas = Tarefa.objects.order_by("id_tarefa")
  lista_tarefas = Tarefa.objects.all().order_by('id_tarefa')

  return render(request, 'html/listar_tarefas.html', {'lista_tarefas': lista_tarefas})

def criar_tarefa(request):
  if request.method == "POST":
    form = TarefaForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_tarefas')
  
  else:
    form = TarefaForm()
  
  return render(request, 'html/form_tarefa.html', {'form': form})

# Esta view recebe o parâmetro "id" que foi definido na rota
def editar_tarefa(request, id):

  # Buscar a tarefa onde o "id_tarefa" seja igual ao parâmetro "id" 
  tarefa = get_object_or_404(Tarefa, id_tarefa = id)
  
  if request.method == "POST":
    form = TarefaForm(request.POST, instance=tarefa)
    if form.is_valid():
      form.save()
      return redirect('listar_tarefas')
  
  else:
    form = TarefaForm(instance=tarefa)
  
  return render(request, 'html/form_tarefa.html', {'form': form})

def excluir_tarefa(request, id):
  # Buscar a tarefa onde o "id_tarefa" seja igual ao parâmetro "id" 
  tarefa = get_object_or_404(Tarefa, id_tarefa = id)
  
  if request.method == "POST":
    tarefa.delete()
    return redirect('listar_tarefas')
  
  return render(request, 'html/excluir_tarefa.html', {'tarefa': tarefa})