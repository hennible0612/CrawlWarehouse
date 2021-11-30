from mallboard.models import Tmon

import csv
def addTmon():
    with open('tmon.csv.csv', encoding='UTF8') as csvfile:
        print("addTmon() 실행")
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            p = Tmon(
                check = row["check"],
                optionNumber = row["optionNumber"],
                orderNum = row["orderNum"],
                shippingCompany = row["shippingCompany"],
                shippingNum = row["shippingNum"],
                expectShipDate = row["expectShipDate"],
                orderDeadLine = row["orderDeadLine"],
                delayedDate = row["delayedDate"],
                delayReason = row["delayReason"],
                delayReasonDetail = row["delayReasonDetail"],
                finalDelayDate = row["finalDelayDate"],
                trackNumApplyDate = row["trackNumApplyDate"],
                sellerCode = row["sellerCode"],
                customerName = row["customerName"],
                customerId = row["customerId"],
                customerCellNum = row["customerCellNum"],
                productName = row["productName"],
                orderOption = row["orderOption"],
                unitPrice = row["unitPrice"],
                orderAmount = row["orderAmount"],
                unitSold = row["unitSold"],
                orderPaymentCompleteDate = row["orderPaymentCompleteDate"],
                orderRequirementsOne = row["orderRequirementsOne"],
                recipientName = row["recipientName"],
                recipientCustomsInfo = row["recipientCustomsInfo"],
                recipientPhoneNum = row["recipientPhoneNum"],
                recipientAddress = row["recipientAddress"],
                postCode = row["postCode"],
                orderRequirements = row["orderRequirements"],
                shipmentState = row["shipmentState"],
                shipmentDate = row["shipmentDate"],
                shipmentArriveDate = row["shipmentArriveDate"],
                partnerCodeOne = row["partnerCodeOne"],
                partnerCodeTwo = row["partnerCodeTwo"],
                partnerCodeThree = row["partnerCodeThree"],
                partnerCodeFour = row["partnerCodeFour"],
                partnerCodeFive = row["partnerCodeFive"],
                optionNumberOne = row["optionNumberOne"],
                remoteAreaDelivery = row["remoteAreaDelivery"],
                remoteAreaDeliveryFee = row["remoteAreaDeliveryFee"],
                shippingFeePayment = row["shippingFeePayment"],
                shippingFee = row["shippingFee"],
                shipping = row["shipping"],
                shippingType = row["shippingType"],
                orderDate = row["orderDate"],
                mallName = row["mallName"],
            )
            p.save()