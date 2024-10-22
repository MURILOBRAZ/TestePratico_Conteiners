from django.shortcuts import render, redirect
from .models import Conteiners, Movimentacao
from .forms import ConteinersForm, MovimentacaoForm
from django.db import models

def home_page(request):
    return render(request, 'home.html')

def criar_conteiner(request):
    if request.method == 'POST':
        form = ConteinersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_conteiner')
    else:
        form = ConteinersForm()
    return render(request, 'criar_conteiner.html', {'form':form})

def listar_conteiner(request):
    conteiner = Conteiners.objects.all()
    return render(request, 'listar_conteiner.html', {'conteiner': conteiner})

def criar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_movimentacao')
    else:
        form = MovimentacaoForm()
    return render(request, 'criar_movimentacao.html', {'form':form})

def listar_movimentacao(request):
    movimentacoes = Movimentacao.objects.all()
    return render(request, 'listar_movimentacao.html', {'movimentacoes': movimentacoes})

def relatorio_movimentacoes(request):
    relatorio = Movimentacao.objects.values('conteiner__cliente','conteiner_id', 'tipo_movimentacao').annotate(total=models.Count('id'))

    total_importacao = Conteiners.objects.filter(categoria='importação').count()
    total_exportacao = Conteiners.objects.filter(categoria='exportação').count()

    return render(request, 'relatorio.html',{
        'relatorio': relatorio,
        'total_importacao': total_importacao,
        'total_exportacao': total_exportacao,
    })

