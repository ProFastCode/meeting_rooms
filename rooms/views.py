from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Room
from .serializers import RoomSerializer
from .filters import RoomFilter


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]  # Для CRUD
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter
