from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    isbn = models.CharField(max_length=15, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    descriptions = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey(Category, related_name= 'books', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    category = models.ForeignKey(Category, related_name='products', on_delete=models.RESTRICT)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{}, {}'.format(self.product_tag, self.name)




