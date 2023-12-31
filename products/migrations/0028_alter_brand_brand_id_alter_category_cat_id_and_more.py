# Generated by Django 4.2.3 on 2023-08-16 08:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('7b274c7d-0a4e-460f-bed8-2daa480e69ce'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('ea16f89f-386c-47f8-a730-432b2164c901'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('ef2b8016-c692-4cce-8167-e1313bbbd6c6'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('26653d1f-f83c-475d-a665-8e2fc6d74e74'), editable=False, primary_key=True, serialize=False),
        ),
    ]
