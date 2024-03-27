# Generated by Django 5.0.3 on 2024-03-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbyte_api', '0007_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('college_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('college_year', models.CharField(max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]