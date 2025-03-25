from django.db import models
from estampa.models import Estampa


class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Tamanho(models.Model):
    TAMANHOS_PRODUTO = [
        ('PP', 'Piquenique'),
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
        ('GG', 'Gigante'),
        ('XG', 'XGigante'),
        ('XXG', 'XXGigante'),
        ('XXXG', 'XXXGigante'),
    ]
        
    tamanho = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id} - {self.tamanho}"


class Produto(models.Model):
    tamanho = models.ManyToManyField(Tamanho, related_name='produto', blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    categorias = models.ManyToManyField(CategoriaProduto, related_name='produtos')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_em_estoque = models.IntegerField(default=0)
    estampas = models.ManyToManyField(Estampa, related_name='produtos', blank=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        tipos_str = ", ".join([tipo.nome for tipo in self.categorias.all()])
        return f'{self.nome} - {tipos_str}'