# Generated by Django 3.2.9 on 2021-11-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mallboard', '0007_alter_coupang_modifiedat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interpark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.TextField(max_length=255)),
                ('recipientAddress', models.TextField(max_length=255)),
                ('serviceUsageFee', models.IntegerField()),
                ('callsafeYn', models.TextField(max_length=255)),
                ('clmreqCnt', models.IntegerField()),
                ('crmCouponDiscountAmount', models.IntegerField()),
                ('currentOrdclmprdStat', models.IntegerField()),
                ('currentOrdclmprdStatNm', models.TextField(max_length=255)),
                ('shippingFee', models.IntegerField()),
                ('orderAmount1', models.IntegerField()),
                ('orderType', models.TextField(max_length=255)),
                ('delvAttbt', models.IntegerField()),
                ('delvAttbtNm', models.TextField(max_length=255)),
                ('orderRequirements', models.TextField(max_length=255)),
                ('delvWhDt', models.TextField(max_length=255)),
                ('delvwhOrdNo', models.TextField(max_length=255)),
                ('delvwhPreDate', models.TextField(max_length=255)),
                ('dtlAddr', models.TextField(max_length=255)),
                ('dtlAddrDoro', models.TextField(max_length=255)),
                ('couponAppliedAmount', models.IntegerField()),
                ('discountAmount', models.IntegerField()),
                ('expectedSellingFee', models.IntegerField()),
                ('expectedSettlementAmt', models.IntegerField()),
                ('sellerCode', models.IntegerField()),
                ('externalPrdNo', models.IntegerField()),
                ('feeRate', models.IntegerField()),
                ('hdelvMafcEntrNoDefault', models.IntegerField()),
                ('inpkCouponDiscountAmount', models.IntegerField()),
                ('interestFreeFee', models.IntegerField()),
                ('ipointDcAmt', models.IntegerField()),
                ('ipointFee', models.IntegerField()),
                ('manufacture', models.TextField(max_length=255)),
                ('marginRate', models.TextField(max_length=255)),
                ('modDelvwhPreDate', models.TextField(max_length=255)),
                ('modDelvwhPreDateYn', models.TextField(max_length=255)),
                ('odpDtlAddr', models.TextField(max_length=255)),
                ('odpDtlAddrDoro', models.TextField(max_length=255)),
                ('odpZipAddr', models.TextField(max_length=255)),
                ('odpZipAddrDoro', models.TextField(max_length=255)),
                ('odpZipNo', models.TextField(max_length=255)),
                ('odpZipNoDoro', models.TextField(max_length=255)),
                ('optFnm', models.TextField(max_length=255)),
                ('optParentSeq', models.IntegerField()),
                ('optPrdTp', models.IntegerField()),
                ('optPrdTpNm', models.TextField(max_length=255)),
                ('orderAmount', models.IntegerField()),
                ('ordEngnm', models.TextField(max_length=255)),
                ('customerId', models.TextField(max_length=255)),
                ('customerCellNum', models.TextField(max_length=255)),
                ('customerName', models.TextField(max_length=255)),
                ('ordSeq', models.IntegerField()),
                ('ordclmDts', models.TextField(max_length=255)),
                ('ordclmNo', models.TextField(max_length=255)),
                ('paidDate', models.TextField(max_length=255)),
                ('parentClaimRequestYn', models.TextField(max_length=255)),
                ('productNum', models.TextField(max_length=255)),
                ('paymentMethod', models.TextField(max_length=255)),
                ('productName', models.TextField(max_length=255)),
                ('productNum1', models.TextField(max_length=255)),
                ('preUseUnitcost', models.TextField(max_length=255)),
                ('unitPrice', models.IntegerField()),
                ('unitSold', models.IntegerField()),
                ('customerPhoneNum', models.TextField(max_length=255)),
                ('recipientName', models.TextField(max_length=255)),
                ('recipientCellNum', models.TextField(max_length=255)),
                ('recipientIdNum', models.TextField(max_length=255)),
                ('residentNo', models.TextField(max_length=255)),
                ('rowNum', models.TextField(max_length=255)),
                ('unitSoldTotal', models.TextField(max_length=255)),
                ('specialYn', models.TextField(max_length=255)),
                ('todayDelvYn', models.TextField(max_length=255)),
                ('totalFee', models.TextField(max_length=255)),
                ('totalPrice', models.TextField(max_length=255)),
                ('totalRecCnt', models.TextField(max_length=255)),
                ('zipAddr', models.TextField(max_length=255)),
                ('zipAddrDoro', models.TextField(max_length=255)),
                ('postCode', models.TextField(max_length=255)),
                ('zipNo', models.TextField(max_length=255)),
                ('zipNoDoro', models.TextField(max_length=255)),
            ],
        ),
    ]