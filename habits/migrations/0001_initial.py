# Generated by Django 5.0.4 on 2024-04-08 11:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(verbose_name='Полезная привычка')),
                ('place', models.CharField(max_length=150, verbose_name='Место выполнения')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата старта привычки')),
                ('start_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время старта привычки')),
                ('deadline', models.TimeField(default='00:00:00', verbose_name='Дедлайн выполнения привычки')),
                ('period', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('in 2 days', 'Каждые 2 дня'), ('in 3 days', 'Каждые 3 дня'), ('in 4 days', 'Каждые 4 дня'), ('in 5 days', 'Каждые 5 дней'), ('in 6 days', 'Каждые 6 дней')], default='daily', max_length=30, verbose_name='Периодичность выполнения')),
                ('reward', models.TextField(blank=True, null=True, verbose_name='Вознаграждение')),
                ('is_nice', models.BooleanField(default=False, verbose_name='Приятная')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='good_habit', to='habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ('id', 'action'),
            },
        ),
    ]
