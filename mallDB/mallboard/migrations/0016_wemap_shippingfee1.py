# Generated by Django 3.2.9 on 2021-12-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0015_wemap'),
    ]

    operations = [
        migrations.AddField(
            model_name='wemap',
            name='shippingFee1',
            field=models.TextField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
