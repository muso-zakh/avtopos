from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, UserCreateSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer
    
    