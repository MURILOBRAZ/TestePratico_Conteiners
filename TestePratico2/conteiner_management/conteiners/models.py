from django.db import models

# Create your models here.
class Conteiners(models.Model):
    cliente = models.CharField(max_length=100, default='Cliente Desconhecido')
    numero_conteiner = models.CharField(max_length=11, unique=True)
    tipo = models.CharField(max_length=3, choices=[('20', '20'), ('40', '40')])
    status = models.CharField(max_length=6, choices=[('cheio', 'Cheio'), ('vazio', 'Vazio')])
    categoria = models.CharField(max_length=12, choices=[('importação', 'Importação'), ('exportação', 'Exportação')])

    def __str__(self):
        return f'Conteiner {self.numero_conteiner}'

class Movimentacao(models.Model):
    MOVIMENTACAO_CHOICES = [
        ('embarque', 'Embarque'),
        ('desembarque', 'Desembarque'),
        ('gate in', 'Gate In'),
        ('gate out', 'Gate Out'),
        ('reposicionamento', 'Reposicionamento'),
        ('pesagem', 'Pesagem'),
        ('scanner', 'Scanner'),
    ]

    conteiner = models.ForeignKey(Conteiners, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(max_length=20, choices=MOVIMENTACAO_CHOICES)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.conteiner.numero_conteiner}"