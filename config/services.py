from django.conf import settings
import requests

NULLABLE = {'null': True, 'blank': True}


class MyBotTest:
    URL = settings.TELEGRAM_URL
    TOKEN = settings.TELEGRAM_TOKEN
    USER_ID = settings.TELEGRAM_USER_ID

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.USER_ID,
                'text': text,
            }
        )
