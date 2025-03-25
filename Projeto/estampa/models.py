from django.db import models

class Estampa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='estampas/', blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"
