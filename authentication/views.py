from .serializers import SignupSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import logout


class SignupView(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "User created successfully",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "message": "Failed to create user",
                "data": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            data = {
                "Message": "User Logged in successfully",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "Message": "Failed to log in user",
                "Error": serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)