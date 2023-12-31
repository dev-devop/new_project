# Generated by Django 4.2.1 on 2023-06-02 08:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderAndCart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(default='no payment', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('canceled', 'canceled')], max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 8, 9, 24, 635244, tzinfo=datetime.timezone.utc)),
        ),
    ]
