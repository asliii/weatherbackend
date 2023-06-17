from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny  # NOQA
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post']

    @action(detail=False, methods=["post"], url_path=r'user_detail',)
    def user_detail(self, request):
        # query = request.GET.get('query', None)  # read extra data
        return Response(self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)
