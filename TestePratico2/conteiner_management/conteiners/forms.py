from django import forms
from .models import Conteiners, Movimentacao

class ConteinersForm(forms.ModelForm):
    class Meta:
        model = Conteiners
        fields = ['cliente', 'numero_conteiner', 'tipo', 'status', 'categoria']
        widgets = {
            'cliente': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            'numero_conteiner': forms.TextInput(attrs={'placeholder': 'Ex: TEST1234567'}),
            'tipo': forms.Select(attrs={'placeholder': '20 ou 40'}),
            'status': forms.Select(attrs={'placeholder': 'Cheio ou Vazio'}),
            'categoria': forms.Select(attrs={'placeholder': 'Importação ou Exportação'}),
        }

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['conteiner', 'tipo_movimentacao', 'data_inicio', 'data_fim']
        widgets = {
            'tipo_movimentacao': forms.Select(attrs={'placeholder': 'Embarque, Desembarque...'}),
            'data_inicio': forms.DateTimeInput(attrs={'placeholder': '2024-12-27 14:30:00'}),
            'data_fim': forms.DateTimeInput(attrs={'placeholder': '2024-12-27 14:30:00'}),
        }