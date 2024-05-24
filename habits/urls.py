from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, UserHabitListAPIView, HabitCreateAPIView, HabitDetailAPIView, \
    HabitUpdateAPIView, HabitDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('my_habits/', UserHabitListAPIView.as_view(), name='my_habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('view/<int:pk>/', HabitDetailAPIView.as_view(), name='habit_view'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_edit'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),
]
