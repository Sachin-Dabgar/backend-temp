# Generated by Django 4.2.3 on 2023-08-16 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('270e06d8-dd3a-4e85-b373-5c93897b8b95'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('5dac5b7a-5ac8-49a7-b864-578c140be096'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('4c77a636-1930-4469-875e-d1f8dc23911b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('3c6ebe4d-4cdc-473c-b72f-aa3a1217dff1'), editable=False, primary_key=True, serialize=False),
        ),
    ]