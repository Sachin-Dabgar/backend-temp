# Generated by Django 4.2.3 on 2023-08-16 15:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0028_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('bf6b5f7e-ee83-4054-9467-55207cca57b3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
