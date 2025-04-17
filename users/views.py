from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignupSerializer, SigninSerializer, MeSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'id': user.id, 'email': user.email})

class LoginView(APIView):
    def post(self, request):
        serializer = SigninSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        tokens = RefreshToken.for_user(user)
        return Response({
            'access_token': str(tokens.access_token),
            'refresh_token': str(tokens)
        })

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = MeSerializer(request.user)
        return Response(user_data.data)

from django.shortcuts import render

# Create your views here.
