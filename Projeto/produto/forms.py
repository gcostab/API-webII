from django import forms
from django.forms import ModelForm
from .models import Produto, CategoriaProduto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categorias', 'preco', 'tamanho', 'quantidade_em_estoque', 'estampas', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control-textarea', 'placeholder': 'Digite a descrição'}),
            'categorias': forms.CheckboxSelectMultiple(attrs={'class': 'form-control-select-multiple'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
            'tamanho': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'required': False}),
            'quantidade_em_estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade em estoque'}),
            'estampas': forms.CheckboxSelectMultiple(attrs={'class': 'form-control-select-checkbox', 'required': False}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CategoriaProdutoForm(ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do tipo de produto'}),
        }