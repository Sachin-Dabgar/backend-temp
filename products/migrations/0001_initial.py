# Generated by Django 4.2.3 on 2023-08-06 07:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.UUIDField(default=uuid.UUID('2e0d26ef-36bc-4ac1-a3f6-33bfd6d787c1'), editable=False, primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=255, unique=True)),
                ('image_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.UUIDField(default=uuid.UUID('f0ae2e47-4cf5-411f-b5e9-54e3a451facc'), editable=False, primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=255, unique=True)),
                ('image_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('sub_id', models.UUIDField(default=uuid.UUID('0f3c6abf-9acc-49d1-a480-ac37d4c45315'), primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=255, unique=True)),
                ('image_data', models.TextField()),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.category')),
            ],
        ),
    ]