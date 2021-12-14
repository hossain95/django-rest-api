from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Category, Book, Product
from main.serializers import CategorySerializer, BookSerializer, ProductSerializer

# Create your views here.



@api_view(['GET'])
def categorys(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    else:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def bookDetail(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def bookDelete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response("Deleted")


@api_view(['GET', 'POST'])
def products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
