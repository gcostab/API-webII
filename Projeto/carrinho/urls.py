from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='carrinho'), # página do carrinho
    path('<int:id>', views.carrinho, name='carrinho'), # página do carrinho do usuário com o id
    path('atualizar_carrinho/', views.atualizar_carrinho, name='atualizar_carrinho'), # atualiza o carrinho
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'), # confirma a compra
]
