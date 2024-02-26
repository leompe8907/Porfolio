from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from . serialize import MyTokenObtainPairSerializar, RegisterUserSerializar

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
       username = data['username'],
       email = data['email'],
       password = make_password(data['password']),
    )
    serializar = RegisterUserSerializar(user, many = False)
    return Response(serializar.data)

class loginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializar
# Create your views here.
