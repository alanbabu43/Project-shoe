# Generated by Django 4.2.1 on 2023-07-20 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_coupon_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancellation_reason',
            field=models.TextField(blank=True),
        ),
    ]
