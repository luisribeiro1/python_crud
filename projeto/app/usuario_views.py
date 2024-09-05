from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all().order_by('id_usuario')
    return render(request, 'html/listar_usuarios.html', {'lista_usuarios': usuarios})

def criar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaUsuarios')
    else:
        form = UsuarioForm()

    return render(request, 'html/form_usuarios.html', {'form': form})

# Esta view recebe o parâmetro "id" que foi definido na rota
def editar_usuario(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    usuarios = get_object_or_404(Usuario, id_usuario=id)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('rotaUsuarios')
    else:
        form = UsuarioForm(instance=usuarios)

    return render(request, 'html/form_usuarios.html', {'form': form})


def excluir_usuario(request, id):

    # Buscar a tarefa onde o id_tarefa seja igual ao parâmetro "id"
    usuarios = get_object_or_404(Usuario, id_usuario=id)

    if request.method == "POST":
        usuarios.delete()
        return redirect('rotaUsuarios')

    return render(request, 'html/excluir_usuarios.html', {'usuarios': usuarios})


