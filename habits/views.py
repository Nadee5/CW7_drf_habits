from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(generics.ListAPIView):
    """Контроллер просмотра списка опубликованных привычек"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        """Фильтруем выборку по признаку публикации"""
        return Habit.objects.filter(is_published=True)


class UserHabitListAPIView(generics.ListAPIView):
    """Контроллер просмотра списка привычек текущего пользователя"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер создания привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitDetailAPIView(generics.RetrieveAPIView):
    """Контроллер просмотра привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер редактирования привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Контроллер удаления привычки"""
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

