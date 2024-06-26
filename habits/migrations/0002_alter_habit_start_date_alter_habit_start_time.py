# Generated by Django 5.0.4 on 2024-04-08 13:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Формат ГГГГ-ММ-ДД', verbose_name='Дата старта привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Формат ЧЧ:ММ:СС', verbose_name='Время старта привычки'),
        ),
    ]
