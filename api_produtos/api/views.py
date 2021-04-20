from django.shortcuts import render
from .models import Tbl_Produtos, Tbl_Inventarios
from .serializers import Tbl_ProdutosSerializer, Tbl_InventariosSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class Tbl_ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Produtos.objects.all()
    serializer_class = Tbl_ProdutosSerializer

class Tbl_InventariosViewSet(viewsets.ModelViewSet):
    queryset = Tbl_Inventarios.objects.all()
    serializer_class = Tbl_InventariosSerializer

    @action(detail=False,url_path="cliente/(?P<cli_id>\d+)")
    def cliente(self,request,cli_id):
        inventarios_list = Tbl_Inventarios.objects.filter(cliente_id=cli_id)
        inventarios_list_serialized = self.get_serializer(inventarios_list, many=True)
        return Response(inventarios_list_serialized.data)