from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    isbn = models.CharField(max_length=15, null=True)
    pages = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    descriptions = models.TextField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name= 'books', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    descriptions = models.TextField(null=True)
    stock = models.IntegerField(null=True)
    status = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{}, {}'.format(self.product_tag, self.name)




