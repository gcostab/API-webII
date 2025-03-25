from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Estampa
from .serializer import EstampaSerializer
from rest_framework import viewsets
from principal.decorators import group_required
from .forms import *

@group_required('Administradores')
@login_required
def listar_estampas(request):
    estampas = Estampa.objects.all()
    return render(request, 'estampa/listar_estampas.html', {'estampas': estampas})


@group_required('Administradores')
@login_required
def create_estampa(request):
    if request.method == "POST":
        form = EstampaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/estampa/')
        else:
            return render(request, "form.html", {"form" : form, 'titulo' : 'Criar Estampa'})
    else:
        form = EstampaForm()
        return render(request, "form.html", {"form" : form, 'titulo' : 'Criar Estampa'})
    

@group_required('Administradores')
@login_required
def edit_estampa(request, id):
    estampa = Estampa.objects.get(pk = id)
    print(estampa)
    if request.method == "POST":
        form = EstampaForm(request.POST, request.FILES, instance=estampa)
        if form.is_valid():
            form.save()
            return redirect('/estampa/')
    else:
        form = EstampaForm(instance=estampa)
        context = {'form' : form, 'titulo' : 'Editar Estampa'}
    if estampa.imagem and hasattr(estampa.imagem, 'url'):
        context['current_image_url'] = estampa.imagem.url
    return render(request, 'form.html', context)


@group_required('Administradores')
@login_required
def remove_estampa(request, id):
    estampa = Estampa.objects.filter(pk = id).first()
    if estampa: estampa.delete()
    return redirect('listar_estampas')

class EstampaViewSet(viewsets.ModelViewSet):
    queryset = Estampa.objects.all()
    serializer_class = EstampaSerializer