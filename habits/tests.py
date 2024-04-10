from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='user@mail.ru', password='12345', is_active=True)
        self.client.force_authenticate(user=self.user)

        """Создание тестовой полезной привычки"""
        self.habit = Habit.objects.create(
            user=self.user,
            action='Тестовая полезная привычка_1',
            place='В случайном месте',
            deadline='20',
        )

    def test_model_habit_str(self):
        habit = Habit.objects.create(action='Написать тест', start_time='20:45:00', place='Комп')

        self.assertEqual(str(habit), 'Привычка: Написать тест, время начать: 20:45:00, место: Комп')

    def test_user_habit_list(self):
        """Тестирование списка привычек для авторизованного пользователя"""
        response = self.client.get(reverse('habits:my_habit_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_published_habit_list(self):
        """Тестирование списка опубликованых привычек"""
        Habit.objects.create(
            user=self.user,
            action='Тестовая полезная привычка_2',
            place='В случайном месте',
            deadline='15',
            is_published=True,
        )
        response = self.client.get(reverse('habits:habit_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            'user': self.user.pk,
            'action': 'Тестовая привычка_3',
            'place': 'В случайном месте',
            'deadline': '30',
        }
        response = self.client.post('/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habit.objects.filter(action=data['action']).exists())

    def test_retrieve_habit(self):
        """Тестирование просмотра привычки"""
        path = reverse('habits:habit_view', [self.habit.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_delete_user_permission(self):
        """Проверка на права доступа: создан пользователь - не владелец привычки"""
        user_2 = User.objects.create(id=2, email='user2@mail.ru', password='1245')
        self.client.force_authenticate(user=user_2)

        path = reverse('habits:habit_delete', [self.habit.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_habit(self):
        """Тестирование удаления привычки владельцем"""
        self.client.force_authenticate(user=self.user)
        path = reverse('habits:habit_delete', [self.habit.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())

    def test_related_or_reward_validator(self):
        """Тестирование создания привычки"""
        data = {
            'user': self.user.pk,
            'action': 'Тестовая привычка_4',
            'place': 'В случайном месте',
            'deadline': '20',
            'reward': self.habit.id,
            'related_habit': self.habit.id,
        }
        response = self.client.post('/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Habit.objects.filter(action=data['action']).exists())

    def test_nice_habit_validator(self):
        """Проверка на отсутствие у приятной привычки полей связанной привычки и вознаграждения"""
        data = {
            'user': self.user.pk,
            'action': 'Тестовая привычка_5',
            'place': 'В случайном месте',
            'deadline': '20',
            'is_nice': True,
            'related_habit': self.habit.id,
        }
        response = self.client.post('/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Habit.objects.filter(action=data['action']).exists())

    def test_deadline_validator(self):
        """Проверка продолжительности выполнения привычки: Должна быть не более 2 минут"""
        data = {
            'user': self.user.pk,
            'action': 'Тестовая привычка_6',
            'place': 'В случайном месте',
            'deadline': '200',
        }
        response = self.client.post('/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Habit.objects.filter(action=data['action']).exists())