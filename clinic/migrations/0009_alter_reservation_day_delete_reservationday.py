# Generated by Django 5.0.6 on 2024-07-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_alter_reservation_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='day',
            field=models.DateField(verbose_name='Day'),
        ),
        migrations.DeleteModel(
            name='ReservationDay',
        ),
    ]
