# Generated by Django 5.0.6 on 2024-07-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(verbose_name='Time'),
        ),
    ]
