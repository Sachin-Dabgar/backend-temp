# Generated by Django 4.2.3 on 2023-08-07 10:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.UUIDField(default=uuid.UUID('f01f494f-dfa6-48e2-a845-d3567473411b'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('account_no', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=11)),
                ('pan_card', models.CharField(max_length=10)),
                ('aadhar_num', models.CharField(max_length=12)),
                ('shipping_address', models.TextField()),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField()),
                ('rating', models.CharField(max_length=2)),
            ],
        ),
    ]
