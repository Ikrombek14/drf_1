from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer

from .models import Category, Author, Books
from rest_framework.response import Response


# Create your views here.

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class Booklist(APIView):
    def get(self, request,):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)



class Bookdetail(APIView):
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)