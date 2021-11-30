import os

from django.core.management.base import BaseCommand

import csv
from mallboard.models import Coupang
def addCoupang():
    os.chdir(r"C:\Users\henni\Desktop\CrawlWarehouse\mallDB\mallboard\myfunction")
    with open('coupang.csv', encoding='UTF8') as csvfile:
        print("addCoupang() 실행")
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            p = Coupang(deliveredDate=row["deliveredDate"], separated=row["separated"],remoteAreaCharge = row["remoteAreaCharge"],
                        shippingNum= row["shippingNum"], parentShipmentBoxId =row["parentShipmentBoxId"], orderNum=row["orderNum"],
                        shippingBundleId =row["shippingBundleId"], customerIdNum=row["customerIdNum"], customerName=row["customerName"],
                        shippingFee = row["shippingFee"], invoiceNumber=row["invoiceNumber"],deliveryStatusCode=row["deliveryStatusCode"],
                        postCode = row["postCode"], orderRequirements=row["orderRequirements"], recipientAddressOne=row["recipientAddressOne"],
                        recipientAddressTwo = row["recipientAddressTwo"], customerCellNum2 = row["customerCellNum2"], customerPhoneNum =row["customerPhoneNum"],
                        recipientName = row["recipientName"], deliverCode = row["deliverCode"], deliverName=row["deliverName"], trackingUrl=row["trackingUrl"],
                        pcpCourier = row["pcpCourier"], pcpContractType = row["pcpContractType"], pcpDelivering = row["pcpDelivering"], pcpDeliverable=row["pcpDeliverable"],
                        productShipmentType = row["productShipmentType"],errorType=row["errorType"], errorMessage =row["errorMessage"], ableSplitShipping = row["ableSplitShipping"],
                        updatedPlannedShippingDate = row["updatedPlannedShippingDate"], coupangFCSellerSendTo =row["coupangFCSellerSendTo"], logistics=row["logistics"],
                        recipientAddress = row["recipientAddress"], giveSecondBool = row["giveSecondBool"], remoteAreaDelivery=row["remoteAreaDelivery"],
                        hasMultipleItems = row["hasMultipleItems"], confirmed = row["confirmed"], createdAt = row["createdAt"], modifiedAt =row["modifiedAt"],
                        customerCellNum1 = row["customerCellNum1"], customerCellNum = row["customerCellNum"], safeNumber=row["safeNumber"], safeNumberSrl = row["safeNumberSrl"],
                        mallName= row["mallName"])
            p.save()