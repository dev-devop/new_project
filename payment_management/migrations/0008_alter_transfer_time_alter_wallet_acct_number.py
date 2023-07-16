# Generated by Django 4.2.1 on 2023-06-09 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_management', '0007_alter_transfer_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 15, 38, 4, 279943, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='acct_number',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]