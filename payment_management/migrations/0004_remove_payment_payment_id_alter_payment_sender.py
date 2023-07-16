# Generated by Django 4.2.1 on 2023-06-07 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment_management', '0003_remove_payment_session_id_alter_payment_payment_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_id',
        ),
        migrations.AlterField(
            model_name='payment',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit', to='payment_management.wallet'),
        ),
    ]
