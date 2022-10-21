from django.shortcuts import render
from rest_framework import viewsets
from .models import Books, Publisher, Category, Author
from .serializers import (
    BookSerializer,
    PublisherSerializer,
    AuthorSerializer,
    CategorySerializer
)


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class CatygoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
