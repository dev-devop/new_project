# Generated by Django 4.2.1 on 2023-06-02 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_management', '0002_alter_destination_destination'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['-is_delivered', 'order'], 'verbose_name_plural': 'Deliveries'},
        ),
    ]
