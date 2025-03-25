from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import login
from rest_framework import viewsets
from .serializers import UserSerializer
from principal.decorators import group_required
from .models import *
from .forms import *

def create_usuario(request):
    if request.method == "POST":
        form = UsuarioFormSingup(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get('password1'))
            user.save()
            login(request, user)
            grupo, created = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo)
            return redirect('home')
        else:
            return render(request, "registration/cadastro.html", {"form" : form, 'titulo' : 'Criar Usuário'})
    else:
        form = UsuarioFormSingup()
        return render(request, "registration/cadastro.html", {"form" : form, 'titulo' : 'Criar Usuário'})

@login_required
def edit_usuario(request, id):
    if not request.user.is_superuser and id != request.user.id:
        return redirect('perfil_usuario')
    usuario = Usuario.objects.filter(pk = id).first()
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            user = form.save()
            if request.user.id == usuario.id:
                login(request, user)
            return redirect('perfil_usuario', id=id)
    else:
        form = UsuarioForm(instance=usuario)
    context = {'form' : form, 'titulo' : 'Editar Usuário'}
    if usuario.imagem and hasattr(usuario.imagem, 'url'):
        context['current_image_url'] = usuario.imagem.url
    return render(request, 'form.html', context)


@login_required
@group_required('Administradores')
def remove_usuario(request, id):
    usuario = Usuario.objects.filter(pk = id).first()
    if usuario: usuario.delete()
    return redirect('listar_usuarios')


@login_required
def perfil(request, id=None):
    if not request.user.is_superuser and id is not None and id != request.user.id:
        return redirect('perfil_usuario')
    user = None
    if id:
        user = get_object_or_404(Usuario, pk=id)
    else:
        user = request.user
    form = UsuarioForm(instance=user)
    return render(request, 'usuario/perfil.html', {'form': form, 'user': user, 'titulo' : 'Perfil do Usuário'})


@login_required
@group_required('Administradores')
def mudar_tipo(request, id):
    if request.method == "POST":
        tipo = request.POST.get('tipo', "Cliente")
        user = get_object_or_404(Usuario, pk=id)
        if tipo == "CLIENTE":
            user.groups.clear()
            user.is_superuser = False
            user.tipo_cliente = tipo
            grupo, created = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo)
        elif tipo == "ADMINISTRADOR":
            user.groups.clear()
            user.tipo_cliente = tipo
            user.is_superuser = True
            grupo, created = Group.objects.get_or_create(name='Administradores')
            user.groups.add(grupo)
        elif tipo == "CORPORATIVO":
            user.groups.clear()
            user.is_superuser = False
            user.tipo_cliente = tipo
            grupo, created = Group.objects.get_or_create(name='Corporativos')
            user.groups.add(grupo)
        user.save()
        messages.success(request, f"Tipo de usuário alterado com sucesso para {Usuario.TIPOS_CLIENTE_DICT[tipo]}.")
    return redirect('perfil_usuario', id=id)


@login_required
@group_required('Administradores')
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})


def receber_suporte_corporativo(request):
    if request.user.groups.filter(name='Administradores').exists():
        return render(request, 'support/receber_suporte_corporativo.html')
    messages.error(request, 'Você não tem permissão para acessar esta página. Para ter uma conta corporativa entre em contato com luni.support@gmail.com')
    return redirect('home')

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer