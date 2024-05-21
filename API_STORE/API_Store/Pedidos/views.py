from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PedidosSerializer
from .models import Comanda
# Create your views here.

@api_view(['GET'])
def historial_comandas(request):
    try:
        comandas = Comanda.objects.all()
        serializer = PedidosSerializer(comandas, many=True)
        return Response({'estado': 'éxito', 'mensaje': 'Historial de comandas mostrado correctamente', 'comandas': serializer.data})
    except Exception as e:
        return Response({'estado': 'error', 'mensaje': str(e)})


@api_view(['GET'])
def historial_comandas_cliente(request, cliente_id):
    try:
        comandas_cliente = Comanda.objects.filter(id_client=cliente_id)
        serializer = PedidosSerializer(comandas_cliente, many=True)
        return Response({'estado': 'éxito', 'mensaje': f'Historial de comandas del cliente {cliente_id} mostrado correctamente', 'comandas': serializer.data})
    except Exception as e:
        return Response({'estado': 'error', 'mensaje': str(e)})


@api_view(['GET'])
def comandas_no_finalizadas(request):
    try:
        comandas_no_finalizadas = Comanda.objects.filter(estado_finalizado=False)
        serializer = PedidosSerializer(comandas_no_finalizadas, many=True)
        return Response({'estado': 'éxito', 'mensaje': 'Historial de comandas no finalizadas mostrado correctamente', 'comandas': serializer.data})
    except Exception as e:
        return Response({'estado': 'error', 'mensaje': str(e)})
