# Generated by Django 4.2.3 on 2023-09-16 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.UUID('b041e6ad-3db3-4326-aa63-044b16dca499'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField()),
            ],
        ),
    ]
