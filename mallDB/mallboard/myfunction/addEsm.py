
from django.core.management.base import BaseCommand
from mallboard.models import Esm
import os
import csv
def addEsm():
    os.chdir(r"C:\Users\henni\Desktop\CrawlWarehouse\mallDB\mallboard\myfunction")
    with open('esm.csv', encoding='UTF8') as csvfile:
        print("addEsm() 실행")
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            p = Esm(
            orderDate =row["orderDate"],
            customerId=row["customerId"],
            mallId =row["mallId"],
            orderNum =row["orderNum"],
            customerName =row["customerName"],
            productNum =row["productNum"],
            productName =row["productName"],
            orderAmount =row["orderAmount"],
            orderOption =row["orderOption"],
            additionalConfig =row["additionalConfig"],
            orderGift =row["orderGift"],
            orderGiftCode =row["orderGiftCode"],
            orderBonus =row["orderBonus"],
            orderBonusCode =row["orderBonusCode"],
            unitPrice =row["unitPrice"],
            unitSold =row["unitSold"],
            sellerCode =row["sellerCode"],
            sellerDetailCode =row["sellerDetailCode"],
            customerCellNum =row["customerCellNum"],
            customerPhoneNum =row["customerPhoneNum"],
            recipientName =row["recipientName"],
            recipientCellNum =row["recipientCellNum"],
            recipientPhoneNum =row["recipientPhoneNum"],
            recipientCustomsInfo =row["recipientCustomsInfo"],
            postCode =row["postCode"],
            recipientAddress =row["recipientAddress"],
            orderRequirements =row["orderRequirements"],
            shippingFeeType =row["shippingFeeType"],
            shippingFee =row["shippingFee"],
            shippingNum =row["shippingNum"],
            shippingPolicy =row["shippingPolicy"],
            skuNum =row["skuNum"],
            deliveryStore =row["deliveryStore"],
            saleType =row["saleType"],
            orderType =row["orderType"],
            shoppingBasketNum =row["shoppingBasketNum"],
            orderPaymentCompleteDate =row["orderPaymentCompleteDate"],
            shipmentDeadline =row["shipmentDeadline"],
            settlementAmount =row["settlementAmount"],
            serviceUsageFee =row["serviceUsageFee"],
            sellerCouponSale =row["sellerCouponSale"],
            couponAppliedAmount =row["couponAppliedAmount"],
            auctionVipDiscount =row["auctionVipDiscount"],
            multiplePurchasesDiscount =row["multiplePurchasesDiscount"],
            smileCash =row["smileCash"],
            sellerCash =row["sellerCash"],
            affiliatedCompany =row["affiliatedCompany"],
            shopSite =row["shopSite"],
            mallName =row["mallName"],

            )

            p.save()


