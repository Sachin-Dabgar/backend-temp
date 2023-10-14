# Generated by Django 4.2.3 on 2023-08-15 10:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('62864222-ac27-443b-891e-69e5c5de120b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('44f17206-e544-44a6-9f17-f53f7cbda07f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('7c6018b9-a258-49c8-a13a-16feba3dfd6d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('97a119cf-7342-4fa4-9cd5-ab3f5d196ffd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
