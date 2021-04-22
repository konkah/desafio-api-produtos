from django.db import models
import requests

class Tbl_Produtos(models.Model):
    nome_produto = models.CharField(max_length=200)
    preco_produto = models.FloatField()
    disponivel_produto = models.BooleanField()

    def __str__(self):
        return self.nome_produto

class Tbl_Inventarios(models.Model):
    produto = models.ForeignKey(Tbl_Produtos, on_delete= models.CASCADE)
    cliente_id = models.IntegerField()

    @property
    def cliente(self):
        url_cliente = "http://172.19.240.1:8000/clientes_api/" + str(self.cliente_id) + "/"
        return requests.get(url_cliente, auth=('admin','admin')).json()

    def __str__(self):
        return self.produto + ' de '+ cliente_id