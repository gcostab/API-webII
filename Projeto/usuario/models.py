from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum
from django.utils.functional import cached_property

class Usuario(AbstractUser):
    TIPOS_CLIENTE_DICT = {
        'CLIENTE': 'Cliente', 
        'CORPORATIVO': 'Corporativo', 
        'ADMINISTRADOR': 'Administrador',
    }
    
    TIPOS_CLIENTE = [
        ('CLIENTE', 'Cliente'),
        ('CORPORATIVO', 'Corporativo'),
        ('ADMINISTRADOR', 'Administrador'),
    ]
    
    qnt_itens = None
    
    imagem = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=20, choices=TIPOS_CLIENTE, default='CLIENTE')
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.id} - {self.username}"
    
    
    def is_admin(self):
        return self.groups.filter(name="Administrador").exists()
    
    def get_size_items(self):
        carrinho = self.carrinho.first()
        if carrinho:
            return carrinho.itens.aggregate(total_items=Sum('quantidade'))['total_items'] or 0
        return 0
