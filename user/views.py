from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def all_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    try:
        email = request.data.get('email',None)
        user  = User.objects.get(email=email)
        return Response('User Already exist')
    except User.DoesNotExist:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)
        
@api_view(['GET', 'PUT', 'DELETE'])
def rud_user(request):
    try:
        user = User.objects.get(user_id=request.data.get.user_id)
        serializer = UserSerializer(user)
    except:
        return Response('User Not Found', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SellerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        seller.delete()
        return Response('User deleted', status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    email = request.data.get('email',None)
    password = request.data.get('password',None)
    try:
        user = User.objects.get(email = email)
        serializer = UserSerializer(user)
        if user.password == password: 
            return Response('user Logged In Successfully')
        else:
            return Response('Invalid Creds')
    except User.DoesNotExist:
        return Response('Invalid Creds')
         
        