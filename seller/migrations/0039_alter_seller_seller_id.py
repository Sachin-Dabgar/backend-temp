# Generated by Django 4.2.3 on 2023-09-28 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0038_alter_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.UUIDField(default=uuid.UUID('79880bfd-1244-483a-a048-4aa68b145677'), editable=False, primary_key=True, serialize=False),
        ),
    ]
