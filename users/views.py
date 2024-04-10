from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения хешированного пароля в БД.
        Если пароль не хешируется - пользователь не считается активным и токен не создаётся"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
