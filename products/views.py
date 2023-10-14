from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import json


# Start of Brand Section


@api_view(['GET'])
def all_brands(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_brand(request):
    try:
        name = request.data.get('brand_name', None)
        brand = Brand.objects.get(brand_name=name)
        return Response('Brand Already exist')
    except Brand.DoesNotExist:
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_brand(request):
    brand_id = request.data.get('brand_id')
    try:
        brand = Brand.objects.get(brand_id=brand_id)
        serializer = BrandSerializer(brand)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        brand.delete()
        return Response('Brand deleted', status=status.HTTP_204_NO_CONTENT)


# End of Brand Section

# Start of Category Section


@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CatSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_category(request):
    try:
        name = request.data.get('cat_name', None)
        category = Category.objects.get(cat_name=name)
        return Response('Category Already exist')
    except Category.DoesNotExist:
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_category(request):
    cat_id = request.data.get('cat_id')
    try:
        category = Category.objects.get(cat_id=cat_id)
        serializer = CatSerializer(category)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CatSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response('Category deleted', status=status.HTTP_204_NO_CONTENT)


# End of Category Section

# Start of Sub Category Section


@api_view(['GET'])
def all_subcategories(request):  # Get all Subcategory
    subcategories = Subcategory.objects.all()
    serializer = SubSerializer(subcategories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_subcategory(request):  # Create Subcategory
    try:
        name = request.data.get('sub_name', None)
        subcategory = Subcategory.objects.get(sub_name=name)
        return Response('Subcategory Already exist')
    except Subcategory.DoesNotExist:
        serializer = SubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_subcategory(request):  # Read,Delete,Update Subcategory
    sub_id = request.data.get('sub_id')
    try:
        subcategory = Subcategory.objects.get(sub_id=sub_id)
        serializer = SubSerializer(subcategory)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubSerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subcategory.delete()
        return Response('Subcategory deleted', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])  # Get Subcategory based on category
def getsubcat(request):
    cid = request.data.get('cat_id')
    try:
        category = Subcategory.objects.filter(cat_id=cid)
        serializer = SubSerializer(category, many=True)
        return Response(serializer.data)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getcatdetails(request):
    categories = Category.objects.all()
    cat_ser = CatSerializer(categories, many=True)
    cat_and_subcats = []
    for i in cat_ser.data:
        subcat = Subcategory.objects.filter(cat_id=i['cat_id'])
        sub_ser = SubSerializer(subcat, many=True)
        temp = [{'sub_id':sub['sub_id'],"sub_name":sub['sub_name']} for sub in sub_ser.data ]
        cat_and_subcats.append({
            'category_id': i['cat_id'],
            'category':i['cat_name'],
            'subcategory':temp
        })   
        final_res = [{'nav_item':"category","sub_items":cat_and_subcats}] 
    return Response(final_res)
# End of Subcategory Section
# Start of Product Section


@api_view(['GET'])
def all_products(request):  # Get all Products
    products = Products.objects.all()
    serializer = ProSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_product(request):  # Create Products
    try:
        name = request.data.get('name')
        seller_id = request.data.get('seller_id')
        product = Products.objects.get(name=name, seller_id=seller_id)
        return Response('Product Already exist')
    except Products.DoesNotExist:
        serializer = ProSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_product(request):  # Read,Delete,Update Product
    pro_id = request.data.get('pro_id')
    try:
        product = Products.objects.get(pro_id=pro_id)
        serializer = ProSerializer(product)
    except:
        return Response('Data not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Products.delete()
        return Response('Product deleted Successfully', status=status.HTTP_204_NO_CONTENT)

# End of Product section

