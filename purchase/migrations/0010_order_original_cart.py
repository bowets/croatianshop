# Generated by Django 3.2.5 on 2021-07-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0009_order_stripe_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default='none'),
        ),
    ]