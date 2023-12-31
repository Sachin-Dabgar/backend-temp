# Generated by Django 4.2.3 on 2023-08-16 15:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('de6f37dc-b32d-4256-9257-451f2d5c949c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('f36235a8-90a5-4578-8469-09dbc33c0cbc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('6b4bfa09-9d7e-4309-a37c-0cf1486cbad3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('5b22d2a1-ae2b-4306-bb8f-b2fe0e9065ae'), editable=False, primary_key=True, serialize=False),
        ),
    ]
