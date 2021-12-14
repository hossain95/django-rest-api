from django.urls import path
from .import views
urlpatterns = [
    path('categorys/', views.categorys, name="categorys"),
    path('books/', views.books, name="books"),
    path('book-detail/<int:pk>/', views.bookDetail, name="book-detail"),
    path('book-update/<int:pk>/', views.bookUpdate, name="book-update"),
    path('book-delete/<int:pk>/', views.bookDelete, name="book-delete"),
    path('products/', views.products, name="products"),
]