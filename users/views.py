# Django Rest Framework
from rest_framework import serializers, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Local Models
from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

class RegisterView(generics.ListCreateAPIView, APIView):

  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer

"""  def post(self, request):
    serializer = UserRegisterSerializer(data=request.data)
    if not serializer.is_valid():
      raise ValueError(status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(serializer.data)"""

class UserView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    serializer = UserSerializer(request.data)
    return Response(serializer.data)
  
  def put(self, request):
    user = User.objects.get(id=request.user.id)
    serializer = UserUpdateSerializer(user, request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
