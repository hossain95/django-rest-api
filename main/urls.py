from django.urls import path
from .import views
urlpatterns = [
    path('categorys/', views.categorys, name="categorys"),
    path('books/', views.books, name="books"),
    path('products/', views.products, name="products"),
]