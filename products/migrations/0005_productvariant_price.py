# Generated by Django 4.2.1 on 2023-06-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productvariant_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
