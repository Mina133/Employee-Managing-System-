from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CustomUser  # Replace with your user model
from .serializers import UserSerializer
from .permissions import AdminOrReadOnly  # Optional: custom permission class

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminOrReadOnly]  # Optional: restrict access to admins

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)