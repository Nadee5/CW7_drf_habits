from django.conf import settings
from django.db import models
from django.utils import timezone

from config.services import NULLABLE


class Habit(models.Model):

    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('in 2 days', 'Каждые 2 дня'),
        ('in 3 days', 'Каждые 3 дня'),
        ('in 4 days', 'Каждые 4 дня'),
        ('in 5 days', 'Каждые 5 дней'),
        ('in 6 days', 'Каждые 6 дней'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь привычки',
                             related_name='user', **NULLABLE)

    action = models.TextField(verbose_name='Полезная привычка')
    place = models.CharField(max_length=150, verbose_name='Место выполнения')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата старта привычки')
    start_time = models.TimeField(default=timezone.now, verbose_name='Время старта привычки')
    deadline = models.TimeField(default='00:00:00', verbose_name='Дедлайн выполнения привычки')

    period = models.CharField(max_length=30, default='daily', choices=PERIOD_CHOICES,
                              verbose_name='Периодичность выполнения')

    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка',
                                      related_name='good_habit', **NULLABLE)
    reward = models.TextField(verbose_name='Вознаграждение', **NULLABLE)

    is_nice = models.BooleanField(default=False, verbose_name='Приятная')
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')

    def __str__(self):
        return f'Привычка: {self.action}, время начать: {self.start_time}, место: {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('id', 'action',)
