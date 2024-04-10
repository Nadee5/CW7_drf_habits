from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from config.services import MyBot, change_start_date


@shared_task
def send_tg_reminder_task():
    """Ежедневное задание: Отправить напоминание о выполнение привычки,
    если дата автозаполнения == сегодняшней"""
    habits = Habit.objects.filter(start_date=timezone.now().date())
    my_bot = MyBot()
    for habit in habits:
        text = f'Напоминаю! Сегодня {habit}'
        chat_id = habit.user.telegram_id
        my_bot.send_message(chat_id, text)
        change_start_date(habit)
