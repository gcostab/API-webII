from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from produto.models import CategoriaProduto, Produto, Tamanho


def home(request):
    """
    View para a página principal do site

    Aceita os seguintes par metros via GET:
        - pesquisa: texto para pesquisar produtos
        - categoria: id da categoria para filtrar produtos
        - preco_min: pre o mínimo para filtrar produtos
        - preco_max: pre o máximo para filtrar produtos
        - tamanho: id do tamanho para filtrar produtos
        - sort: ordena o dos produtos (preco_asc ou preco_desc)

    Retorna uma lista de produtos filtrada e ordenada de acordo com os parâmetros
    e uma lista de categorias para o menu de categorias do site.
    """
    produtos = Produto.objects.all()
    
    # Filtros
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
    
    # Paginação
    paginator = Paginator(produtos, 12)  # Mostra 10 produtos por página
    page = request.GET.get('page')
    
    try:
        produtos_pagina = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exiba a primeira página.
        produtos_pagina = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (por exemplo, 9999), exiba a última página de resultados.
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
    
    if request.user.is_authenticated:
        if request.user.tipo_cliente == "ADMINISTRADOR" or request.user.is_superuser:
            request.user.groups.clear()
            request.user.tipo_cliente = "ADMINISTRADOR"
            request.user.is_superuser = True
            grupo, created = Group.objects.get_or_create(name='Administradores')
            request.user.groups.add(grupo)
            
        elif request.user.tipo_cliente is None or request.user.tipo_cliente == "":
            request.user.groups.clear()
            request.user.is_superuser = False
            grupo, created = Group.objects.get_or_create(name='Corporativos')
            request.user.groups.add(grupo)
                
        else:
            request.user.groups.clear()
            request.user.is_superuser = False
            grupo, created = Group.objects.get_or_create(name='Corporativos')
            request.user.groups.add(grupo)
                
        request.user.save()
    
    return render(request, 'principal/home.html', context)


@login_required
def settings(request):
    """
    View para a página de configurações do site
    """
    return render(request, 'principal/settings.html', {})