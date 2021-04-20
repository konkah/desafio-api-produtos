from django.db import models


class Tbl_Produtos(models.Model):
    nome_produto = models.CharField(max_length=200)
    preco_produto = models.FloatField()
    disponivel_produto = models.BooleanField()

    def __str__(self):
        return self.nome_produto

class Tbl_Inventarios(models.Model):
    produto = models.ForeignKey(Tbl_Produtos, on_delete= models.CASCADE)
    cliente_id = models.IntegerField()

    def __str__(self):
        return self.produto + ' de '+ cliente_id