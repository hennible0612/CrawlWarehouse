# Generated by Django 3.2.9 on 2021-11-23 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpark',
            name='orderDate',
            field=models.DateField(),
        ),
    ]
