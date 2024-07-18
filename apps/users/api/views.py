from rest_framework import viewsets
from apps.users.models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCreateSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer
