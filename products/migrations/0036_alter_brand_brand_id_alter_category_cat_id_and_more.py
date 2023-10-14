# Generated by Django 4.2.3 on 2023-09-16 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('2a6eeb2a-61a1-477f-903c-3caafe552342'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('60559e66-f6f8-4382-bdd4-749a503bd64a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('ce4882d7-e4b6-4a71-8fad-a5f7c4ffbc65'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('a6f156dd-2f7c-4b95-8f87-ea52a118099a'), editable=False, primary_key=True, serialize=False),
        ),
    ]