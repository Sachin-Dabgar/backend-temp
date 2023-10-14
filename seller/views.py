from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def all_sellers(request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_seller(request):
    try:
        number = request.data.get('phone',None)
        seller = Seller.objects.get(phone=number)
        return Response('Seller Already exist')
    except Seller.DoesNotExist:
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def rud_seller(request, phone):
    try:
        seller = Seller.objects.get(phone=phone)
        serializer = SellerSerializer(seller)
    except:
        return Response('Seller Not Found', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        seller.delete()
        return Response('Seller deleted', status=status.HTTP_204_NO_CONTENT)

