from django.db import models


# Create your models here.
class Coupang(models.Model):
    deliveredDate = models.TextField(null=True, max_length=255)
    separated = models.TextField(null=True)
    remoteAreaCharge = models.IntegerField(null=True)
    shippingNum = models.IntegerField()
    parentShipmentBoxId = models.IntegerField()
    orderNum = models.TextField(max_length=255)
    shippingBundleId = models.TextField(max_length=255)
    customerIdNum = models.IntegerField()
    customerName = models.TextField(max_length=255)
    shippingFee = models.IntegerField()
    invoiceNumber = models.TextField(null=True)
    deliveryStatusCode = models.TextField(null=True)
    postCode = models.IntegerField()
    orderRequirements = models.TextField()
    recipientAddressOne = models.TextField()
    recipientAddressTwo = models.TextField()
    customerCellNum2 = models.TextField(null=True, max_length=255)
    customerPhoneNum = models.TextField(null=True, max_length=255)
    recipientName = models.TextField(max_length=255)
    deliverCode = models.TextField(max_length=255)
    deliverName = models.TextField(max_length=255)
    trackingUrl = models.TextField(max_length=255)
    pcpCourier = models.TextField(max_length=255)
    pcpContractType = models.TextField(max_length=255)
    pcpDelivering = models.TextField(max_length=255)
    pcpDeliverable = models.TextField(max_length=255)
    productShipmentType = models.TextField(max_length=255)
    errorType = models.TextField(max_length=255)
    errorMessage = models.TextField(max_length=255)
    ableSplitShipping = models.TextField(max_length=255)
    updatedPlannedShippingDate = models.TextField(max_length=255)
    coupangFCSellerSendTo = models.TextField(max_length=255)
    logistics = models.TextField(max_length=255)
    recipientAddress = models.TextField(max_length=255)
    giveSecondBool = models.TextField(max_length=255)
    remoteAreaDelivery = models.TextField(max_length=255)
    hasMultipleItems = models.TextField(max_length=255)
    confirmed = models.TextField(max_length=255)
    createdAt = models.TextField(max_length=255)
    modifiedAt = models.TextField(max_length=255)
    customerCellNum1 = models.IntegerField()
    customerCellNum = models.IntegerField()
    safeNumber = models.IntegerField()
    safeNumberSrl = models.TextField(max_length=255)
    mallName = models.TextField(max_length=255,default='쿠팡')

    def __str__(self):
        return " 주문자 : "+self.customerName + " 주소  : " + self.recipientAddress

    class Meta:
       ordering = ['-id']

class Interpark(models.Model):
    orderDate = models.DateField()
    recipientAddress = models.TextField(max_length=255)
    serviceUsageFee = models.TextField(max_length=255)
    callsafeYn = models.TextField(max_length=255)
    clmreqCnt = models.IntegerField()
    crmCouponDiscountAmount = models.IntegerField()
    currentOrdclmprdStat = models.IntegerField()
    currentOrdclmprdStatNm = models.TextField(max_length=255)
    shippingFee = models.TextField(max_length=255)
    orderAmount1 = models.TextField(max_length=255)
    orderType = models.TextField(max_length=255)
    delvAttbt = models.IntegerField()
    delvAttbtNm = models.TextField(max_length=255)
    orderRequirements = models.TextField(max_length=255)
    delvWhDt = models.TextField(max_length=255)
    delvwhOrdNo = models.TextField(max_length=255)
    delvwhPreDate = models.TextField(max_length=255)
    dtlAddr = models.TextField(max_length=255)
    dtlAddrDoro = models.TextField(max_length=255)
    couponAppliedAmount = models.TextField(max_length=255)
    discountAmount = models.IntegerField()
    expectedSellingFee = models.IntegerField()
    expectedSettlementAmt = models.IntegerField()
    sellerCode = models.IntegerField()
    externalPrdNo = models.IntegerField()
    feeRate = models.IntegerField()
    hdelvMafcEntrNoDefault = models.IntegerField()
    inpkCouponDiscountAmount = models.IntegerField()
    interestFreeFee = models.IntegerField()
    ipointDcAmt = models.IntegerField()
    ipointFee = models.IntegerField()
    manufacture= models.TextField(max_length=255)
    marginRate = models.TextField(max_length=255)
    modDelvwhPreDate = models.TextField(max_length=255)
    modDelvwhPreDateYn = models.TextField(max_length=255)
    odpDtlAddr= models.TextField(max_length=255)
    odpDtlAddrDoro= models.TextField(max_length=255)
    odpZipAddr= models.TextField(max_length=255)
    odpZipAddrDoro= models.TextField(max_length=255)
    odpZipNo= models.TextField(max_length=255)
    odpZipNoDoro= models.TextField(max_length=255)
    optFnm = models.TextField(max_length=255)
    optParentSeq = models.IntegerField()
    optPrdTp = models.IntegerField()
    optPrdTpNm = models.TextField(max_length=255)
    orderAmount = models.IntegerField()
    ordEngnm = models.TextField(max_length=255)
    customerId = models.TextField(max_length=255)
    customerCellNum = models.TextField(max_length=255)
    customerName = models.TextField(max_length=255)
    ordSeq = models.IntegerField()
    customerCellNum2 = models.TextField(null=True, max_length=255)
    ordclmDts = models.TextField(max_length=255)
    ordclmNo = models.TextField(max_length=255)
    paidDate = models.TextField(max_length=255)
    parentClaimRequestYn = models.TextField(max_length=255)
    productNum = models.TextField(max_length=255)
    paymentMethod = models.TextField(max_length=255)
    productName = models.TextField(max_length=255)
    productNum1 = models.TextField(max_length=255)
    preUseUnitcost = models.TextField(max_length=255)
    unitPrice = models.IntegerField()
    unitSold = models.IntegerField()
    customerPhoneNum = models.TextField(max_length=255)
    recipientName = models.TextField(max_length=255)
    recipientCellNum = models.TextField(max_length=255)
    recipientIdNum = models.TextField(max_length=255)
    residentNo = models.TextField(max_length=255)
    rowNum = models.TextField(max_length=255)
    unitSoldTotal = models.TextField(max_length=255)
    specialYn = models.TextField(max_length=255)
    todayDelvYn = models.TextField(max_length=255)
    totalFee = models.TextField(max_length=255)
    totalPrice = models.TextField(max_length=255)
    totalRecCnt = models.TextField(max_length=255)
    zipAddr = models.TextField(max_length=255)
    zipAddrDoro = models.TextField(max_length=255)
    postCode = models.TextField(max_length=255)
    zipNo = models.TextField(max_length=255)
    zipNoDoro = models.TextField(max_length=255)
    mallName = models.TextField(max_length=255,default='인터파크')

    def __str__(self):
        return " 주문자 : "+self.customerName + " 주소  : " + self.recipientAddress

    class Meta:
       ordering = ['-id']

class Esm(models.Model):







    def __str__(self):
        return " 주문자 : " + self.customerName + " 주소  : " + self.recipientAddress

    class Meta:
        ordering = ['-id']