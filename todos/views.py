from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Category, Task


class CategoryView(APIView):
    permission_classes = []
    authentication_classes = []

    serializer_class = CategorySerializer

    # handling get requests 
    def get(self, request):
        categories = [category.name for category in Category.objects.all()]
        return Response(categories)

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