from .models import Produto, CategoriaProduto
from rest_framework import serializers

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
class CategoriaProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProduto
        fields = '__all__'