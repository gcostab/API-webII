from django.urls import path
from . import views

urlpatterns = [
    path('add-carrinho/<int:id>/', views.adicionar_ao_carrinho, name='add_carrinho'), # adiciona um item ao carrinho
    path('<int:id>/', views.detalhes_produto, name='detalhes_produto'), # detalhes de um item
    path('rm-carrinho/<int:id>/', views.remover_do_carrinho, name='rm_carrinho'), # remove um item do carrinho
    path('listar/produtos/', views.listar_produtos, name='listar_produtos'), # lista de produtos
    path('listar/tipos/', views.listar_tipos_produtos, name='listar_tipo_produtos'), # lista de categorias
    path('pesquisa/', views.pesquisar_produtos, name='pesquisar_produto'), # pesquisa de produtos
    path('create/', views.create_produto, name='create_produto'), # cria um novo produto
    path('update/<int:id>/', views.edit_produto, name='edit_produto'), # edita um produto
    path('delete/<int:id>/', views.remove_produto, name='delete_produto'), # deleta um produto
    path('tipo/create/', views.create_tipo_produto, name='create_tipo_produto'), # cria uma nova categoria
    path('tipo/update/<int:id>/', views.edit_tipo_produto, name='edit_tipo_produto'), # edita uma categoria
    path('tipo/delete/<int:id>/', views.remove_tipo_produto, name='delete_tipo_produto'), # deleta uma categoria
]