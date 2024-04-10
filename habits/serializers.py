from rest_framework import serializers
from habits.models import Habit
from habits.validators import RelatedOrRewardValidator, NiceHabitValidator, RelatedHabitValidator, \
    DeadlineValidator


class HabitSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedOrRewardValidator(),
            NiceHabitValidator(),
            RelatedHabitValidator(),
            DeadlineValidator(),
        ]
