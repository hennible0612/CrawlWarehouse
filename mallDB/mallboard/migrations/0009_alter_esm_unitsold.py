# Generated by Django 3.2.9 on 2021-12-01 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0008_alter_esm_unitprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esm',
            name='unitSold',
            field=models.TextField(max_length=255),
        ),
    ]