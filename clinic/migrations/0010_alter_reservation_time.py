# Generated by Django 5.0.6 on 2024-07-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_alter_reservation_day_delete_reservationday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Time'),
        ),
    ]
