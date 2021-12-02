# Generated by Django 3.2.9 on 2021-12-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0010_alter_esm_shippingfee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esm',
            name='sellerCash',
        ),
        migrations.AddField(
            model_name='esm',
            name='sellerCas',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='affiliatedCompany',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='shippingNum',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='smileCash',
            field=models.TextField(max_length=255, null=True),
        ),
    ]