# Generated by Django 5.1.7 on 2025-03-13 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0005_alter_feedback_feedback_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='Booking_Time',
            field=models.TimeField(default=datetime.time(19, 0)),
        ),
        migrations.AddField(
            model_name='booktable',
            name='Cab_Required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booktable',
            name='Pickup_Coordinates',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booktable',
            name='Pickup_Location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
