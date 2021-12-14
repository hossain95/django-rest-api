from rest_framework import serializers
from main.models import Product, Category, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = (
        #     'id',
        #     'title',
        #     'isbn',
        #     'pages',
        #     'price',
        #     'stock',
        #     'descriptions',
        #     'status',
        #     'date_created',
        # )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = (
        #     'id',
        #     'product_tag',
        #     'name',
        #     'price',
        #     'quantity',
        #     'descriptions',
        #     'stock',
        #     'status',
        #     'date_created',
        # )