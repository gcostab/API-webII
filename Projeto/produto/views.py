from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from carrinho.models import Carrinho, ItemCarrinho
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from rest_framework import viewsets
from .serializers import ProdutoSerializers, CategoriaProdutoSerializers
from principal.decorators import group_required
from .models import *
from .forms import *


@login_required
def detalhes_produto(request, id):
    produto = Produto.objects.filter(id=id).first()
    if not produto:
        return redirect('listar_produtos')
    return render(request, 'produto/produto.html', {'produto': produto})


@login_required
@group_required('Administradores')
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/listar_produtos.html', {'produtos': produtos})


@login_required
@group_required('Administradores')
def listar_tipos_produtos(request):
    form_tipo = CategoriaProdutoForm()
    tipos_produtos = CategoriaProduto.objects.all()
    return render(request, 'produto/listar_tipos_produtos.html', {"tipo_produto_form": form_tipo, "tipos_produtos": tipos_produtos})


@login_required
@group_required('Administradores')
def create_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
        else:
            return render(request, "form.html", {"form" : form, 'titulo': 'Criar produto'})
    else:
        form = ProdutoForm()
        return render(request, "form.html", {"form" : form, 'titulo': 'Criar produto'})


@login_required
@group_required('Administradores')
def edit_produto(request, id):
    produto = Produto.objects.get(pk = id)
    print(produto)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    context = {'form' : form, 'titulo' : 'Editar produto'}
    if produto.imagem and hasattr(produto.imagem, 'url'):
        context['current_image_url'] = produto.imagem.url
    return render(request, 'form.html', context)


@login_required
@group_required('Administradores')
def remove_produto(request, id):
    produto = Produto.objects.filter(pk = id)
    if produto: produto.delete()
    return redirect('listar_produtos')


@login_required
@group_required('Administradores')
def create_tipo_produto(request):
    if request.method == "POST":
        form = CategoriaProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_tipo_produtos")
        else:
            return redirect("listar_tipo_produtos")
    else:
        form = CategoriaProdutoForm()
        return redirect("listar_tipo_produtos")

@login_required
@group_required('Administradores')
def edit_tipo_produto(request, id):
    categoriaProduto = CategoriaProduto.objects.get(pk = id)
    print(categoriaProduto)
    if request.method == "POST":
        form = CategoriaProdutoForm(request.POST, instance=categoriaProduto)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_produtos')
    else:
        form = CategoriaProdutoForm(instance=categoriaProduto)
    return render(request, "form.html", {'form' : form, 'titulo': 'Editar tipo de produto'})


@login_required
@group_required('Administradores')
def remove_tipo_produto(request, id):
    categoriaProduto = CategoriaProduto.objects.filter(pk = id).first()
    if categoriaProduto: categoriaProduto.delete()
    return redirect('listar_tipo_produtos')


def pesquisar_produtos(request):
    produtos = Produto.objects.all()
    pesquisa = request.GET.get('pesquisa', '').strip()
    categoria_id = request.GET.get('categoria')
    preco_min = request.GET.get('preco_min')
    preco_max = request.GET.get('preco_max')
    tamanho_id = request.GET.get('tamanho')
    sort = request.GET.get('sort', '')
    
    if sort == 'preco_asc':
        produtos = produtos.order_by('preco')
    elif sort == 'preco_desc':
        produtos = produtos.order_by('-preco')
    if pesquisa:
        produtos = produtos.filter(Q(nome__icontains=pesquisa) | Q(descricao__icontains=pesquisa))
    if categoria_id:
        produtos = produtos.filter(categorias__id=categoria_id)
    if preco_min:
        produtos = produtos.filter(preco__gte=preco_min)
    if preco_max:
        produtos = produtos.filter(preco__lte=preco_max)
    if tamanho_id:
        produtos = produtos.filter(tamanho__id=tamanho_id)

    paginator = Paginator(produtos, 12)  
    page = request.GET.get('page')
    
    try:
        produtos_pagina = paginator.page(page)
    except PageNotAnInteger:
        produtos_pagina = paginator.page(1)
    except EmptyPage:
        produtos_pagina = paginator.page(paginator.num_pages)
    categorias = CategoriaProduto.objects.all()
    tamanhos = Tamanho.objects.all()
    context = {
        'produtos': produtos_pagina,
        'categorias': categorias,
        'tamanhos': tamanhos,
        'pesquisa': pesquisa,
        'preco_min': preco_min,
        'preco_max': preco_max,
        'categoria_id': int(categoria_id if categoria_id else 0),
        'tamanho_id': int(tamanho_id if tamanho_id else 0),
        'sort': sort,
    }
    return render(request, 'produto/pesquisa.html', context)


@login_required
def adicionar_ao_carrinho(request, id):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=id)
        usuario = request.user
        carrinho, created = Carrinho.objects.get_or_create(usuario=usuario)
        quantidade = int(request.POST.get('quantidade'))
        estampa_id = request.POST.get('estampa')
        tamanho_id = request.POST.get('tamanho')
        estampa = None
        tamanho = None
        
        if estampa_id is not None:
            estampa_id = int(estampa_id)
            estampa = get_object_or_404(Estampa, id=estampa_id)
        if tamanho_id is not None:
            tamanho_id = int(tamanho_id)
            tamanho = get_object_or_404(Tamanho, id=tamanho_id)
        
        item, created = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho, 
            produto=produto, 
            estampa=estampa, 
            tamanho=tamanho, 
            defaults={'quantidade': quantidade}
        )
        if not created:
            item.quantidade += quantidade
            item.save()
    return redirect('carrinho')


@login_required
def remover_do_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    usuario = request.user
    carrinho, created = Carrinho.objects.get_or_create(usuario=usuario)
    item_carrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    
    if item_carrinho:
        item_carrinho.delete()
    return redirect('carrinho')

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers
    
class CategoriaProdutoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaProdutoSerializers