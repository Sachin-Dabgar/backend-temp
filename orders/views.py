from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



@api_view(['GET'])
def all_orders(requests):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

    
@api_view(['POST'])
def add_order(request):
    try:
        user_id = request.data.get('user_id')
        pro_id = request.data.get('pro_id')
        data = Order.objects.get(user_id = user_id, pro_id=pro_id)
        return Response('Product already in orders')
    except Order.DoesNotExist:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
@api_view(['POST'])
def add_cart(request):
    try:
        user_id = request.data.get('user_id')
        pro_id = request.data.get('pro_id')
        cart_data = Cart.objects.get(user_id = user_id, pro_id=pro_id)
        return Response('Product already in cart')
    except Cart.DoesNotExist:
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def all_cart(request):
    cart_data = Cart.objects.all()
    serializer = CartSerializer(cart_data, many=True)
    return Response(serializer.data)    
    
@api_view(['GET','PUT','DELETE'])
def rud_cart(request):
    cart_id = request.data.get('cart_id')
    try:
        cart = Cart.objects.get(cart_id=cart_id)
        serializer = CartSerializer(cart)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cart.delete()
        return Response('cart item deleted Successfully', status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def display_cart(request):
    user_id = request.data.get('user_id')
    data = Cart.calculate_total_price(user_id)
    if data != None:
        serializers = CartSerializer(data[0], many=True)
        data = {'data':serializers.data,'total':data[1]}
        return Response(data)
    else:
        return('No items in cart')


@api_view(['POST'])
def add_wish(request):
    try:
        user_id = request.data.get('user_id')
        pro_id = request.data.get('pro_id')
        wishlist = Wishlist.objects.get(user_id = user_id, pro_id=pro_id)
        return Response('Product already in wishlist')
    except Wishlist.DoesNotExist:
        serializer = WishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def all_wish(request):
    wish_data = Wishlist.objects.all()
    serializer = WishSerializer(wish_data, many=True)
    return Response(serializer.data)    
    
@api_view(['GET','PUT','DELETE'])
def rd_wish(request):
    wish_id = request.data.get('wish_id')
    try:
        wishlist = Wishlist.objects.get(wish_id=wish_id)
        serializer = WishSerializer(wishlist)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'DELETE':
        wishlist.delete()
        return Response('Item removed from wishlist', status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def display_wish(request):
    user_id = request.data.get('user_id')
    try:
        wish = Wishlist.objects.filter(user_id= user_id)
        serializer = WishSerializer(wish, many=True)
        return Response(serializer.data)
    except Wishlist.DoesNotExist:
        return Response('Wishlist is empty')

