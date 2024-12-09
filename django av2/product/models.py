from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=False)
    descricao = models.CharField(max_length=500, null=False)
    valor = models.FloatField(null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
