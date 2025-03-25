from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pedido, ItemPedido
from .serializer import ItemPedidoSerializer, PedidoSerializer
from rest_framework import viewsets
from principal.decorators import group_required
from .models import *
from .forms import *


@login_required
def listar_pedidos(request, id=None):
    if id:
        if not request.user.is_superuser and id != request.user.pk:
            redirect('listar_pedidos', request.user.pk)
        user = get_object_or_404(Usuario, pk=id)
        pedidos = Pedido.objects.filter(cliente=user)
    elif request.user.is_superuser:
        pedidos = Pedido.objects.all()
    else:
        redirect('listar_pedidos', request.user.pk)
    return render(request, 'pedido/listar_pedidos.html', {'pedidos': pedidos})


@login_required
@group_required('Administradores')
def create_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pedido/')
        else:
            return render(request, "form.html", {"form" : form, 'titulo' : 'Criar pedido'})
    else:
        form = PedidoForm()
        return render(request, "form.html", {"form" : form, 'titulo' : 'Criar pedido'})

@login_required
@group_required('Administradores')
def edit_pedido(request, id):
    pedido = Pedido.objects.get(pk = id)
    print(pedido)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('/pedido/')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'form.html', {'form' : form, 'titulo': 'Editar pedido'})


@login_required
@group_required('Administradores')
def remove_pedido(request, id):
    pedido = Pedido.objects.filter(pk=id).first()

    if not pedido:
        messages.error(request, 'Pedido não encontrado.')
        return redirect("listar_pedidos")

    pedido.delete()
    return redirect('listar_pedidos')


@login_required
def pedido(request, id):
    pedido = Pedido.objects.filter(pk=id).first()
    if not pedido:
        messages.error(request, 'Pedido não encontrado.')
        return redirect("listar_pedidos")
    if request.user.is_superuser or request.user.id == pedido.cliente.id:
        itens = ItemPedido.objects.filter(pedido=pedido)
        return render(request, 'pedido/pedido.html', {'pedido': pedido, 'itens': itens})
    messages.error(request, 'Você não tem permissão para acessar esta página.')
    return redirect("listar_pedidos")

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    
    
