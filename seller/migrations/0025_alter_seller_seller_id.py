# Generated by Django 4.2.3 on 2023-08-16 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0024_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('11575fcb-826e-4444-9f3b-1cc6ed619352'), editable=False, primary_key=True, serialize=False),
        ),
    ]
