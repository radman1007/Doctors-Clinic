# Generated by Django 5.0.6 on 2024-07-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_reservationday_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='doctor',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
