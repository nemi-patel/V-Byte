# Generated by Django 5.0.3 on 2024-03-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbyte_api', '0006_alter_game_student_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('online', 'Online')], max_length=10)),
                ('cheque_photo', models.ImageField(blank=True, null=True, upload_to='cheque/')),
            ],
        ),
    ]
