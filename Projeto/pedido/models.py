from django.db import models

from usuario.models import Usuario
from produto.models import *

class Pedido(models.Model):
    STATUS_PEDIDO = [
        ('PROCESSANDO', 'Processando'),
        ('ENVIADO', 'Enviado'),
        ('ENTREGUE', 'Entregue'),
    ]

    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateTimeField(auto_now_add=True)
    itens = models.ManyToManyField(Produto, through='ItemPedido')
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO, default='PROCESSANDO')

    def __str__(self):
        return f'{self.id} - {self.cliente.username}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedido')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, blank=True, null=True)
    estampa = models.ForeignKey(Estampa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'
