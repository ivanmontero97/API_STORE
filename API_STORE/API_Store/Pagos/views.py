from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PagosSerializer
from Pedidos.serializer import PedidosSerializer
from Pedidos.serializer import Comanda
from .models import Producto
# Create your views here.


@api_view(['POST'])
def get_datos_pago(request, pk):
    try:
        comanda = Comanda.objects.get(pk=pk)
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST' and not comanda.estado_finalizado:
        data_serializer = PagosSerializer(data=request.data)
        if data_serializer.is_valid():
            try:
                data_serializer.save()
                comanda.estado_finalizado = True
                comanda.save()
                return Response({"data": data_serializer.data, "comanda_estado": comanda.estado_finalizado}, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "La comanda ya está finalizada o el método no es POST"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def consultar_estado_comanda(request, pk):
    try:
        comanda = Comanda.objects.get(pk=pk)
    except Comanda.DoesNotExist:
        return Response({"error": "Comanda no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PedidosSerializer(comanda)
    return Response(serializer.data, status=status.HTTP_200_OK)