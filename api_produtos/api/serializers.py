from rest_framework import serializers
from .models import Tbl_Produtos, Tbl_Inventarios

class Tbl_ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Produtos
        fields = '__all__'

class Tbl_InventariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbl_Inventarios
        fields = '__all__'