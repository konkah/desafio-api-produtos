from rest_framework import serializers
from .models import Tbl_Produtos, Tbl_Inventarios

class Tbl_ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Produtos
        fields = [
            'nome_produto', 
            'preco_produto', 
            'disponivel_produto',
        ]

class Tbl_InventariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Inventarios
        fields = [
            'produto', 
            'cliente',
        ]
        depth = 1

    def validate_produto_id(produto_id):
        produto = Tbl_Produtos.objects.get(pk = produto_id)
        if not produto.disponivel_produto:
            raise serializers.ValidationError(
                'Produto não disponível para compra.'
            )