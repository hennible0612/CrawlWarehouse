# Generated by Django 3.2.9 on 2021-11-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0010_alter_interpark_serviceusagefee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interpark',
            name='shippingFee',
            field=models.TextField(max_length=255),
        ),
    ]