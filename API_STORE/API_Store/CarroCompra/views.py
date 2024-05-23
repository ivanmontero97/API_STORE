from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CarretoSerializer,ListaProductosSerializer,UpdateUnitatsSerializer
from .models import Carreto,ListaProductos
from Catalago.models import *
from Pedidos.models import *
# Create your views here.

@api_view(['POST'])
def add_Carreto(request):
    cliente_id = request.data.get('id_client')
    if Carreto.objects.filter(id_client=cliente_id, estat='abierto').exists():
        return Response({"message": "No se puede crear un nuevo carrito porque ya hay uno abierto para este cliente"}, status=status.HTTP_400_BAD_REQUEST)
    
    data_serializer = CarretoSerializer(data=request.data)
    
    if data_serializer.is_valid():
        data_serializer.save()
        id_client = data_serializer.validated_data['id_client']
        estat = data_serializer.validated_data['estat']
        cliente = Cliente.objects.get(pk=id_client.id)
        cliente_data = {
            "id": cliente.id,
            "nombre": cliente.nombre,
            "apellidos": cliente.apellidos,
            "email": cliente.email
        }
        return Response({
            "message": "Carrito creado correctamente",
            "data": {
                "cliente": cliente_data,
                "estado": estat
            }
        }, status=status.HTTP_201_CREATED)
    
    return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_Products(request):
    data_serializer = ListaProductosSerializer(data=request.data)

    if data_serializer.is_valid():
        carreto_estat = data_serializer.validated_data['id_carreto'].estat
        if(carreto_estat == 'abierto'):
            # Verificar si hay suficiente stock del producto
            producto_id = data_serializer.validated_data['producto'].id
            unitats = data_serializer.validated_data['unitats']
            producto = get_object_or_404(Producto, pk=producto_id)
            if producto.stock < unitats:
                return Response({"message": "No hay suficiente stock del producto"}, status=status.HTTP_400_BAD_REQUEST)

            data_serializer.save()
            return Response({"data": data_serializer.data, "message": "Producto agregado al carreto correctamente"}, status=status.HTTP_201_CREATED)
        return Response({'El estado del carrito seleccionado esta cerrado y no se pueden agregar productos'})
    return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_Producto(request, pk_product):
    # Buscar el producto por su ID (pk)
    producto = get_object_or_404(ListaProductos, pk=pk_product)
    carreto_estat = producto.id_carreto.estat
    if(carreto_estat == 'abierto'):
        # Eliminar el producto
        producto.delete()

        return Response({"message": "Producto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    return Response({'El estado del carrito seleccionado esta cerrado y no se pueden eliminar productos'},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_AllProductsFromLista(request, pk_carreto):
    # Obtener el carreto por su ID
    carreto = get_object_or_404(Carreto, pk=pk_carreto)
    if(carreto.estat == 'abierto'):
        # Eliminar todos los productos
        carreto.delete()

        return Response({"message": "El carreto y todos los productos asociado han sido eliminados correctamente"}, status=status.HTTP_204_NO_CONTENT)
    return Response({'El estado del carrito seleccionado esta cerrado y no se puede eliminar'},status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_product_quantity(request, pk_product):
    # Obtener el producto por su ID (pk)
    productoLista = get_object_or_404(ListaProductos, pk=pk_product)
    if(productoLista.id_carreto.estat == 'abierto'):
        stock_producto = productoLista.producto.stock
        # Actualizar la cantidad de unidades
        serializer = UpdateUnitatsSerializer(productoLista, data=request.data, partial=True)  # partial=True para permitir actualización parcial
        if serializer.is_valid():
            if(serializer.validated_data['unitats'] <= stock_producto ):
                serializer.save()
                return Response({"data": serializer.data, "message": "Cantidad actualizada correctamente"}, status=status.HTTP_200_OK)
            return Response({"Error":"La cantidad seleccionada no puede ser superior al stock del producto"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'El carreto seleccionado se encuentra en estado cerrado y no se pueden modificar las cantidades de sus productos'},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_products_in_carreto(request, pk_carreto):
    # Obtener el carreto por su ID
    carreto = get_object_or_404(Carreto, pk=pk_carreto)
    # Obtener todos los productos asociados a este carreto
    productos = ListaProductos.objects.filter(id_carreto=carreto)
    # Serializar los datos
    serializer = ListaProductosSerializer(productos, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_estat_carreto(request, pk_carreto):
    # Obtener el carreto por su ID (pk)
    carreto = get_object_or_404(Carreto, pk=pk_carreto)
    # Verificar si el estado actual del carreto es 'abierto'
    if carreto.estat == 'abierto':
        # Cambiar el estado a 'cerrado'
        carreto.estat = 'cerrado'
        carreto.save()
        return Response({"message": "Estado del carreto actualizado correctamente a 'cerrado'"}, status=status.HTTP_200_OK)
    else:
        # El estado ya está 'cerrado', no hacer ningún cambio
        return Response({"message": "El estado del carreto ya está 'cerrado', no se realizaron cambios"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def comprar(request, pk_carreto):
    # Obtener el carreto por su ID
    carreto = get_object_or_404(Carreto, pk=pk_carreto)
    
    if carreto.estat != 'abierto':
        return Response({"message": "El carreto ya está cerrado y no se puede comprar"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Obtener todos los productos asociados a este carreto
    productos = ListaProductos.objects.filter(id_carreto=carreto)
    
    if not productos.exists():
        return Response({"message": "El carreto no tiene productos"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Actualizar el stock de cada producto
    for producto_lista in productos:
        producto = producto_lista.producto
        if producto.stock < producto_lista.unitats:
            return Response({"message": f"No hay suficiente stock para el producto {producto.nombre}"}, status=status.HTTP_400_BAD_REQUEST)
        
        producto.stock -= producto_lista.unitats
        producto.save()
    
    # Cambiar el estado del carreto a 'cerrado'
    carreto.estat = 'cerrado'
    carreto.save()
    
    # Crear una comanda con la información del carreto
    comanda = Comanda.objects.create(
        id_carreto=carreto,
        id_client=carreto.id_client,
        estado_finalizado=True
    )
    
    # Serializar los productos del carreto
    productos_serializer = ListaProductosSerializer(productos, many=True)
    
    # Preparar la respuesta con la información necesaria
    response_data = {
        "message": "Compra realizada correctamente",
        "carreto": CarretoSerializer(carreto).data,
        "comanda": {
            "id": comanda.id,
            "id_carreto": comanda.id_carreto.id,
            "id_client": comanda.id_client.id,
            "estado_finalizado": comanda.estado_finalizado,
            "created_at": comanda.created_at,
            "updated_at": comanda.updated_at,
        },
        "productos": productos_serializer.data,
        "precio_total": sum(p.producto.precio * p.unitats for p in productos)
    }
    
    return Response(response_data, status=status.HTTP_200_OK)