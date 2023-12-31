# Generated by Django 4.2.3 on 2023-08-15 12:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('30fd42fe-94b3-4f9d-bfa8-c3d6ea1591e3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('66ea9389-b764-4a38-9327-9f76f1d48b9b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('9d84855c-f482-48b8-a584-cb2b28856de8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('414a9559-1530-44b5-a45e-2266176a0b67'), editable=False, primary_key=True, serialize=False),
        ),
    ]
