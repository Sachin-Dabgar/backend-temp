# Generated by Django 4.2.3 on 2023-09-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(editable=False, max_length=25),
        ),
    ]