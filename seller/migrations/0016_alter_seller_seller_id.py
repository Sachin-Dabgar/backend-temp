# Generated by Django 4.2.3 on 2023-08-15 13:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0015_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('ff48471c-9cb5-4a17-b81d-177ed9bd1882'), editable=False, primary_key=True, serialize=False),
        ),
    ]