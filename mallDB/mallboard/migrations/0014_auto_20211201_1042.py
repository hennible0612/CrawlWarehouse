# Generated by Django 3.2.9 on 2021-12-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0013_alter_interpark_serviceusagefee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esm',
            name='auctionVipDiscount',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='couponAppliedAmount',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='multiplePurchasesDiscount',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='sellerCouponSale',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='esm',
            name='serviceUsageFee',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
