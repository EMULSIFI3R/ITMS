# Generated by Django 5.1.2 on 2024-11-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0006_driver_nfc_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='nfc_code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
