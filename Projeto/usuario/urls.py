from django.urls import path
from . import views

urlpatterns = [
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'), # lista de usuários
    path('<int:id>/mudar_tipo/', views.mudar_tipo, name='mudar_tipo'), # muda o tipo de usuário
    path('perfil/<int:id>/', views.perfil, name='perfil_usuario'), # perfil do usuário
    path('perfil/', views.perfil, name='perfil_usuario'), # perfil do usuário
    path('create/', views.create_usuario, name='create_usuario'), # cria um novo usuário
    path('update/<int:id>/', views.edit_usuario, name='edit_usuario'), # edita um usuário
    path('delete/<int:id>/', views.remove_usuario, name='delete_usuario'), # remove um usuário
    path('receber_suporte_corporativo/', views.receber_suporte_corporativo, name='receber_suporte_corporativo'), # TODO: recebe suporte


]


