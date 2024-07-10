# Generated by Django 5.0.6 on 2024-07-10 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0015_alter_reservation_day_delete_reservationday'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Reservation Day',
                'verbose_name_plural': 'Reservation Days',
                'ordering': ('-date',),
            },
        ),
        migrations.AlterField(
            model_name='freereservation',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.reservationday'),
        ),
    ]
