# Generated by Django 4.2.1 on 2023-06-10 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_management', '0008_alter_transfer_time_alter_wallet_acct_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 10, 22, 7, 45, 719032, tzinfo=datetime.timezone.utc)),
        ),
    ]
