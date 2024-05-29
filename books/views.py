from django.shortcuts import render
from rest_framework import status
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


class BookDelete(APIView):
    def delete(self, request, pk):
        try:
            books=Books.objects.get(id=pk)
            books.delete()
            serializer_data = {
                "books":"deleted successfully",
                "status":"success",
                "status_code":status.HTTP_200_OK,
            }
        except Exception as e:
            serializer_data = {
                "error":str(e),
                "status":"failed",
                "status_code":status.HTTP_404_NOT_FOUND,
            }
        finally:
            return Response(serializer_data)


class BookUpdate(APIView):
    def put(self, request, pk):
        try:
            books=Books.objects.get(id=pk)
            serializer = BookSerializer(books, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "books":"updated successfully",
                    "status":"success",
                    "status_code":status.HTTP_200_OK,
                }
        except Exception as e:
            serializer_data = {
                "error":str(e),
                "status":"failed",
                "status_code":status.HTTP_404_NOT_FOUND,
            }
        finally:
            return Response(serializer_data)

    def patch(self, request, pk):
        try:
            books=Books.objects.get(id=pk)
            serializer = BookSerializer(books, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "books":"updated successfully",
                    "status":"success",
                    "status_code":status.HTTP_200_OK,
                }
        except Exception as e:
            serializer_data = {
                "error":str(e),
                "status":"failed",
                "status_code":status.HTTP_404_NOT_FOUND,
            }
        finally:
            return Response(serializer_data)
