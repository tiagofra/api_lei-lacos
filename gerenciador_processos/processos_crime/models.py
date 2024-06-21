from django.db import models

from django.db import models

class Processo(models.Model):
    # CATEGORIAS_CHOICES = [
    #     ('criminal', 'Criminal'),
    #     ('trabalhista', 'Trabalhista'),
    #     ('legislativo', 'Legislativo'),
    #     ('consumidor', 'Consumidor'),
    #     ('ambiental', 'Ambiental'),
    #     ('digital', 'Digital'),
    #     ('empresarial', 'Empresarial'),
    #     ('eleitoral', 'Eleitoral'),
    # ]

    cpfExecutado = models.CharField(max_length=11, default="")
    nomeExecutado = models.CharField(max_length=100, default="")
    advogadoExecutado = models.CharField(max_length=100, default="")
    oabAdvExecutado = models.CharField(max_length=100, default="")

    nomeExequente = models.CharField(max_length=100, default="")
    cpfExequente = models.CharField(max_length=100, default="")
    advogadoExequente = models.CharField(max_length=100, default="")
    oabAdvExequente = models.CharField(max_length=100, default="")

    descricaoCaso = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    natureza = models.CharField(max_length=100, default="")
    poderJudiciario = models.CharField(max_length=100, default="")
    local = models.CharField(max_length=100, default="")
    STATUS_CHOICES = (
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
        ('arquivado', 'Arquivado'),
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return self.nomeCliente