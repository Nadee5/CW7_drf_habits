from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='user@mail.ru', password='12345', is_active=True)
        self.client.force_authenticate(user=self.user)

    def test_model_user_str(self):
        """Тестирование представления __str__ у модели"""

        self.assertEqual(str(self.user), 'user@mail.ru')
