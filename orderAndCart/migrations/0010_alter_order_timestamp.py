# Generated by Django 4.2.1 on 2023-06-07 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderAndCart', '0009_alter_order_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 7, 8, 40, 57, 808359, tzinfo=datetime.timezone.utc)),
        ),
    ]
