# Generated by Django 4.2.3 on 2023-09-18 06:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('27a086eb-c75f-4077-abb0-d5f5ff9c7fe2'), editable=False, primary_key=True, serialize=False),
        ),
    ]
