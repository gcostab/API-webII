from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from estampa.views import EstampaViewSet
from usuario.views import UserViewSet
from carrinho.views import CarrinhoViewSet, ItemCarrinhoViewSet
from pedido.views import ItemPedidoViewSet, PedidoViewSet
from produto.views import ProdutoViewSet, CategoriaProdutoViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'estampas', EstampaViewSet)
router.register(r'usuario', UserViewSet)
router.register(r'carrinho', CarrinhoViewSet)
router.register(r'item-carrinho', ItemCarrinhoViewSet)
router.register(r'pedido', PedidoViewSet)
router.register(r'item-pedido', ItemPedidoViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'categoria', CategoriaProdutoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)