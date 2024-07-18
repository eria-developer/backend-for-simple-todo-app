from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Category, Task
from rest_framework.generics import get_object_or_404


class CategoryListApiView(APIView):
    # handling get requests 
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # handling post requests 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "Message": "Category added successfully",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "Message": "Failed to add category",
                "data": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryDetailApiView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)
    
    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "Message": "Details updated successfully",
                "Data": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "Message": "Failed to update category details",
                "Error": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)