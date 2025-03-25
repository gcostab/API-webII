from produto.models import CategoriaProduto

def variaveis_globais(request):
    var = {
        'nome_site': 'Luni',
        'categorias': CategoriaProduto.objects.all(),
    }
    
    return var