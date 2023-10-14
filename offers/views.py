from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import *
from django.utils import timezone

@api_view(['GET'])
def today_deal(request):
    recent_products = Products.objects.order_by('listed_date')[:10]
    serializer = ProSerializer(recent_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def offers(request):
    products = Products.objects.filter(discount_offers__startswith='O_')[:10]
    serializer = ProSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def featured_data(request):
    products = Products.objects.all().order_by('?')[:7]
    serializer = ProSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def today_deal_cat(request, cat_id):
#     recent_products = Products.objects.latest('listed_date')
#     five_days_ago = timezone.now() - timezone.timedelta(days=5)
#     # products = Products.objects.filter(cat_id=cat_id, listed_date__lt=recent_products.listed_date, listed_date__gte=five_days_ago)
#     serializer = ProSerializer(recent_products, many=True)
#     return Response(serializer.data)

