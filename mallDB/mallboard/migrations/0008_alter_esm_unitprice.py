# Generated by Django 3.2.9 on 2021-12-01 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0007_naver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esm',
            name='unitPrice',
            field=models.TextField(max_length=255),
        ),
    ]
