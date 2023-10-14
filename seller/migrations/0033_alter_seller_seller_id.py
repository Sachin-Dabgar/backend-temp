# Generated by Django 4.2.3 on 2023-09-16 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0032_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('d55e41ba-726c-450d-b3ac-a025890b531e'), editable=False, primary_key=True, serialize=False),
        ),
    ]
