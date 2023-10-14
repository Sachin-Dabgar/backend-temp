# Generated by Django 4.2.3 on 2023-08-15 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_brand_brand_id_alter_category_cat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_id',
            field=models.UUIDField(default=uuid.UUID('667f38c7-1d26-4fad-b26b-a2f701e55e81'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.UUIDField(default=uuid.UUID('e5bd46e4-8635-46da-bcb5-4c51d2cab485'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='pro_id',
            field=models.UUIDField(default=uuid.UUID('5171ab03-05de-4b60-88e4-c0a23e1a8275'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_id',
            field=models.UUIDField(default=uuid.UUID('b407ea01-6109-4c81-b55b-00e5e15f2511'), editable=False, primary_key=True, serialize=False),
        ),
    ]
