from time import sleep
import os
from mallboard.models import Wemap



import csv
def addWemap():

    os.chdir(r"C:\Users\henni\Desktop\CrawlWarehouse\mallDB\mallboard\myfunction")
    with open('Wemap.csv', encoding='UTF8') as csvfile:
        print("addWemap() 실행")
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

            p = Wemap(
                addShipPrice = row["addShipPrice"],
                recipientAddress1 = row["recipientAddress1"],
                recipientAddress2 = row["recipientAddress2"],
                addrInfo = row["addrInfo"],
                allCount = row["allCount"],
                shippingNum = row["shippingNum"],
                bundleShipMethod = row["bundleShipMethod"],
                customerName = row["customerName"],
                customerCellNum = row["customerCellNum"],
                claimBundleNo = row["claimBundleNo"],
                commissionPriceTotal = row["commissionPriceTotal"],
                companyCd = row["companyCd"],
                companyNm = row["companyNm"],
                orderPaymentCompleteDate = row["orderPaymentCompleteDate"],
                confirmDt = row["confirmDt"],
                d4MaskingYn = row["d4MaskingYn"],
                delayShipCd = row["delayShipCd"],
                delayShipDt = row["delayShipDt"],
                delayShipMessage = row["delayShipMessage"],
                delayShipNm = row["delayShipNm"],
                failCount = row["failCount"],
                failList = row["failList"],
                failMessage = row["failMessage"],
                invoiceNo = row["invoiceNo"],
                isReply = row["isReply"],
                isSupportWmpCommission = row["isSupportWmpCommission"],
                isSupportWmpPrice = row["isSupportWmpPrice"],
                issuePhone = row["issuePhone"],
                maskingYn = row["maskingYn"],
                orderRequirements = row["orderRequirements"],
                mid = row["mid"],
                multiShipNo = row["multiShipNo"],
                multiShippingYn = row["multiShippingYn"],
                orderDate = row["orderDate"],
                shoppingBasketNum = row["shoppingBasketNum"],
                orderOptNo = row["orderOptNo"],
                orderType = row["orderType"],
                shipmentDeadline = row["shipmentDeadline"],
                shippingFee1 = row["shippingFee1"],
                partDeliveryYn = row["partDeliveryYn"],
                partnerId = row["partnerId"],
                recipientCustomsInfo = row["recipientCustomsInfo"],
                recipientCellNum = row["recipientCellNum"],
                prepaymentYn = row["prepaymentYn"],
                shippingFeeType = row["shippingFeeType"],
                productName = row["productName"],
                orderNum = row["orderNum"],
                unitPrice = row["unitPrice"],
                orderAmount = row["orderAmount"],
                purchaseNo = row["purchaseNo"],
                recipientName = row["recipientName"],
                requestChannel = row["requestChannel"],
                requestDate = row["requestDate"],
                requestReasonDetail = row["requestReasonDetail"],
                requestReasonType = row["requestReasonType"],
                requestReasonTypeNm = row["requestReasonTypeNm"],
                scheduleShipDt = row["scheduleShipDt"],
                sellerOptCd = row["sellerOptCd"],
                sellerCode = row["sellerCode"],
                shipAddrNo = row["shipAddrNo"],
                shipAreaType = row["shipAreaType"],
                shipCompleteDt = row["shipCompleteDt"],
                shipMethod = row["shipMethod"],
                shipMethodNm = row["shipMethodNm"],
                shipNo = row["shipNo"],
                shippingFee = row["shippingFee"],
                shipStatus = row["shipStatus"],
                shipStatusNm = row["shipStatusNm"],
                shippingArgumentNo = row["shippingArgumentNo"],
                shippingDt = row["shippingDt"],
                soptTitle = row["soptTitle"],
                successCount = row["successCount"],
                unitSold = row["unitSold"],
                uploadCode = row["uploadCode"],
                uploadFailMessage = row["uploadFailMessage"],
                wmpAffiliateRate = row["wmpAffiliateRate"],
                postCode = row["postCode"],
                mallName = row["mallName"],
            )
            p.save()