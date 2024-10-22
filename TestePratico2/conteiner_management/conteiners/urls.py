from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('conteiners/', views.listar_conteiner, name='listar_conteiner'),
    path('conteiners/novo', views.criar_conteiner, name='criar_conteiner'),
    path('movimentacoes/', views.listar_movimentacao, name='listar_movimentacao'),
    path('movimentacoes/nova', views.criar_movimentacao, name='criar_movimentacao'),
    path('relatorio/', views.relatorio_movimentacoes, name='relatorio'),
]