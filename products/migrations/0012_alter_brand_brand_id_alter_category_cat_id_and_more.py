# Generated by Django 4.2.3 on 2023-08-15 12:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('b9323851-4f29-494d-97a7-cc21d128ad2b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('0e237cfc-18a4-4871-b9b3-75d44759c005'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('cbc6475f-d2bf-4405-8aa7-b468bc4fce62'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('3513be98-bc99-4b13-84f4-8fa07bb974da'), editable=False, primary_key=True, serialize=False),
        ),
    ]
