from time import sleep
import os
from mallboard.models import Naver



import csv
def addNaver():

    os.chdir(r"C:\Users\henni\Desktop\CrawlWarehouse\mallDB\mallboard\myfunction")
    with open('naver.csv', encoding='UTF8') as csvfile:
        print("addNaver() 실행")
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            p = Naver(
                check = row["check"],
                orderNum = row["orderNum"],
                orderDate = row["orderDate"],
                shopSite = row["shopSite"],
                customerName = row["customerName"],
                customerId = row["customerId"],
                recipientName = row["recipientName"],
                shippingState = row["shippingState"],
                orderState = row["orderState"],
                shopMachine = row["shopMachine"],
                orderTime = row["orderTime"],
                productName = row["productName"],
                producetState = row["producetState"],
                optionInfo = row["optionInfo"],
                optionSellerCode = row["optionSellerCode"],
                orderAmount = row["orderAmount"],
                optionPrce = row["optionPrce"],
                unitNormalPrice = row["unitNormalPrice"],
                saleAmount = row["saleAmount"],
                sellerSaleAmount = row["sellerSaleAmount"],
                unitPrice = row["unitPrice"],
                gift = row["gift"],
                shipmentDeadline = row["shipmentDeadline"],
                shippingFeeType = row["shippingFeeType"],
                shippingFeeSate = row["shippingFeeSate"],
                shippingFee = row["shippingFee"],
                remoteAreaDeliveryFee = row["remoteAreaDeliveryFee"],
                shippingSale = row["shippingSale"],
                sellerCode = row["sellerCode"],
                customerCellNum = row["customerCellNum"],
                recipientAddress = row["recipientAddress"],
                customerPhoneNum = row["customerPhoneNum"],
                postCode = row["postCode"],
                orderRequirements = row["orderRequirements"],
                payType = row["payType"],
                shopMarket = row["shopMarket"],
                searchType = row["searchType"],
                mallName = row["mallName"],

            )
            p.save()