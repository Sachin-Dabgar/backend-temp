# Generated by Django 4.2.3 on 2023-08-15 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0017_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('bbba5d8d-99eb-4feb-947a-7e2ec1cf78db'), editable=False, primary_key=True, serialize=False),
        ),
    ]
