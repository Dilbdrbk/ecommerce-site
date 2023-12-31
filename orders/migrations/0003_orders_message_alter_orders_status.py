# Generated by Django 4.2.7 on 2023-12-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orders_mobile_numbers_alter_orders_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('shipped', 'shipped'), ('cancelled', 'cancelled'), ('delivered', 'delivered'), ('pending', 'pending')], default='pending', max_length=50),
        ),
    ]
