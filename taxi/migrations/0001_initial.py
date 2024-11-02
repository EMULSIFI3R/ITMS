# Generated by Django 5.1 on 2024-10-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeTaxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=20, unique=True)),
                ('color', models.CharField(default='Unknown Color', max_length=50)),
                ('model', models.CharField(default='Unknown Model', max_length=50)),
                ('capacity', models.IntegerField(default=4)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]