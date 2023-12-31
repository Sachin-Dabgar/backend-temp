# Generated by Django 4.2.3 on 2023-08-16 15:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('1af67083-7fa3-49ff-8fd4-42a39d17c390'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('9bfd7ac6-457c-4a12-8043-b742e783b208'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('d06cbd4e-e30d-451c-bcc1-f83de3ccaa23'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('64bb17f2-593a-44e5-a22b-0d125d9a84ac'), editable=False, primary_key=True, serialize=False),
        ),
    ]
