# Generated by Django 4.2.3 on 2023-08-15 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('2865a4cd-68f4-4f77-a9a2-76b99844e475'), editable=False, primary_key=True, serialize=False),
        ),
    ]
