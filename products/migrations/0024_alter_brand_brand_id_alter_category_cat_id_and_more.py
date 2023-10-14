# Generated by Django 4.2.3 on 2023-08-15 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('520c727c-f67f-4715-a5e2-5fcabf9d6ff3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('129da1c5-7076-4ef2-966a-f31a7a4278df'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('63974bb0-1473-472b-a15c-43e5e77659c7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('3863bd18-3ea1-44a1-9a16-11a076a878e5'), editable=False, primary_key=True, serialize=False),
        ),
    ]
