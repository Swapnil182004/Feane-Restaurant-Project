# Generated by Django 5.1.7 on 2025-03-12 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone_Number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Person_Number', models.IntegerField()),
                ('Booking_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=30)),
                ('Feedback_Description', models.TextField()),
                ('Rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=25)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='Items/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Name', to='Base_App.itemlist')),
            ],
        ),
    ]
