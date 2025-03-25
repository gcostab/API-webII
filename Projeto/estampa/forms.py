from django import forms
from django.forms import ModelForm
from .models import Estampa

class EstampaForm(ModelForm):
    class Meta:
        model = Estampa
        fields = ['nome', 'descricao', 'imagem', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control', 'placeholder': 'Digite o nome da estampa'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control form-control-textarea', 'placeholder': 'Digite a descrição'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a categoria'}),
        }