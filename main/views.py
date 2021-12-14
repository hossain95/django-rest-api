from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Category, Book, Product
from main.serializers import CategorySerializer, BookSerializer, ProductSerializer


@api_view(['Get'])
def categorys(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['Get'])
def books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)

@api_view(['Get'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
