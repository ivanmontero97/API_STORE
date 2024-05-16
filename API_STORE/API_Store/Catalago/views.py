from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from .models import Producto
# Create your views here.

@api_view(['GET'])
def get_prod(request):
    product_list = Producto.objects.all()
    data_serializer = ProductSerializer(product_list, many = True)
    return Response({'data': data_serializer.data})

@api_view(['GET'])
def get_prod_By_Id(request, pk):
    product = Producto.objects.get(id=pk)
    data_serializer = ProductSerializer(product, many= False)
    return Response ({"data": data_serializer.data})


@api_view(['POST', 'PUT'])
def add_or_update_prod(request):
    if request.method == 'POST':
        data_serializer = ProductSerializer(data=request.data)
        
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({"data": data_serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        try:
            product_id = request.data.get('id')
            product = Producto.objects.get(id=product_id)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        data_serializer = ProductSerializer(product, data=request.data)
        
        if data_serializer.is_valid():
            data_serializer.save()
            return Response({"data": data_serializer.data}, status=status.HTTP_200_OK)
        
        return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_stock(request, pk ):
        try:
            new_stock = request.data["new_stock"]
            product = Producto.objects.get(id=pk)
            product.stock = new_stock
            product.save()
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
     
        return Response(f"Producto actualizado a stock : {product.stock}")

@api_view(['GET'])
def isValid(resquest, pk):
    try: 
        product = Producto.objects.get(id=pk)
        product.isActive = True
        product.save()
    except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
     
    return Response(f"Producto borrado logico : {product.isActive}")

@api_view(['GET'])
def isnotValid(resquest, pk):
    try: 
        product = Producto.objects.get(id=pk)
        product.isActive = False
        product.save()
    except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
     
    return Response(f"Producto borrado logico : {product.isActive}")

