# Generated by Django 4.2.3 on 2023-08-15 10:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('bce92e97-a774-42a5-a833-09a8c421aabd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
