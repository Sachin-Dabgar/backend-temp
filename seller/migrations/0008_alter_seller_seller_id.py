# Generated by Django 4.2.3 on 2023-08-15 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('825b1e0e-be61-4fc6-b468-fe2d52bd4e1b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
