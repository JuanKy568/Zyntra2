from rest_framework import viewsets
from .models import Usuario, Avatar
from .serializers import UsuarioSerializer, AvatarSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        usuario = request.user.usuario
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)