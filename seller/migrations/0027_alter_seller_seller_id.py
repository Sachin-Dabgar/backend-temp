# Generated by Django 4.2.3 on 2023-08-16 08:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0026_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('ca0f8859-970e-4318-b97f-648159c5f200'), editable=False, primary_key=True, serialize=False),
        ),
    ]
