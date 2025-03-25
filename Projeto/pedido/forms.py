from django import forms
from django.forms import ModelForm
from .models import Pedido, ItemPedido

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'itens', 'preco_total', 'status']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control-select'}),
            'itens': forms.CheckboxSelectMultiple(attrs={'class': 'form-control-select-chekbox'}),
            'preco_total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço total'}),
            'status': forms.Select(attrs={'class': 'form-control-select'}),
        }
        

class ItemPedidoForm(ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'produto', 'quantidade', 'preco']
        widgets = {
            'pedido': forms.Select(attrs={'class': 'form-control-select'}),
            'produto': forms.Select(attrs={'class': 'form-control-select'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
        }