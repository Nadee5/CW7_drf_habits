from django.core.management import BaseCommand

from config.services import MyBotTest


class Command(BaseCommand):

    def handle(self, *args, **options):
        my_bot = MyBotTest()
        my_bot.send_message('Hi, Sky!')
