from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Producto
# Create your views here.

@api_view(['GET'])
def get_prod(request):
    product_list = Producto.objects.all()
    data_serializer = ProductSerializer(product_list, many = True)
    return Response({'data': data_serializer.data})

@api_view(['GET'])
def get_prod_By_Id(request):
    return 

@api_view(['POST'])
def add_prod(request):
    return

