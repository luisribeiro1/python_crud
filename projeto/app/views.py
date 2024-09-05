from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
from .forms import Usuario
from .forms import UsuarioForm

def listar_tarefas(request):
    
    #tarefas = Tarefa.objects.all().order_by('id_tarefa')
    #Recupera o termo usado no campo da busca

    query = request.GET.get('q')
    if query:
        tarefas = Tarefa.objects.filter(titulo__icontains=query)
    else:
        tarefas = Tarefa.objects.all().order_by('id_tarefa')    


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

# Esta view recebe o parâmetro "id" que foi definido na rota
def editar_tarefa(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    tarefa = get_object_or_404(Tarefa, id_tarefa=id)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('rotaTarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'html/form_tarefa.html', {'form': form})


def excluir_tarefa(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    tarefa = get_object_or_404(Tarefa, id_tarefa=id)

    if request.method == "POST":
        tarefa.delete()
        return redirect('rotaTarefas')

    return render(request, 'html/excluir_tarefa.html', {'tarefa': tarefa})


def criar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaUsuarios')
    else:
        form = UsuarioForm()

    return render(request, 'html/form_usuario.html', {'form': form})

# Esta view recebe o parâmetro "id" que foi definido na rota
def editar_usuario(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    usuario = get_object_or_404(Usuario, id_usuario=id)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('rotaUsuarios')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'html/form_usuario.html', {'form': form})  

def excluir_usuario(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    usuario = get_object_or_404(Usuario, id_usuario=id)

    if request.method == "POST":
        usuario.delete()
        return redirect('rotaUsuarios')

    return render(request, 'html/excluir_usuario.html', {'usuario': usuario})      


