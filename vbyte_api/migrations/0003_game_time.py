# Generated by Django 5.0.3 on 2024-03-22 05:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbyte_api', '0002_game_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]