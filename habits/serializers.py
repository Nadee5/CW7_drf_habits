from rest_framework import serializers
from habits.models import Habit
from habits.validators import deadline_validator, RelatedOrRewardValidator, NiceHabitValidator, RelatedHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели привычки"""
    deadline = serializers.TimeField(validators=[deadline_validator])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedOrRewardValidator(),
            NiceHabitValidator(),
            RelatedHabitValidator(),
        ]
