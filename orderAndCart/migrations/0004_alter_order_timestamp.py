# Generated by Django 4.2.1 on 2023-06-02 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderAndCart', '0003_alter_ordereditem_options_remove_ordereditem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 8, 16, 51, 288295, tzinfo=datetime.timezone.utc)),
        ),
    ]
