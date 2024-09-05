from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'html/listar_usuarios.html', {'lista_usuarios': usuarios})

def criar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotaUsuarios')
    else:
        form = UsuarioForm()

    return render(request, 'html/form_usuario.html', {'form': form})


def editar_usuario(request, id):

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


    usuario = get_object_or_404(Usuario, id_usuario=id)

    if request.method == "POST":
        usuario.delete()
        return redirect('rotaUsuarios')


    return render(request, 'html/excluir_usuario.html', {'usuario': usuario})
