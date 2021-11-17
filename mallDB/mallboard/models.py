from django.db import models

# Create your models here.
class Coupang(models.Model):
    deliveredDate = models.TextField(null=True, max_length=255)
    separated = models.TextField(null=True)
    remoteAreaCharge = models.IntegerField(null=True)
    shippingNum = models.IntegerField()
    parentShipmentBoxId = models.IntegerField()
    orderNum = models.IntegerField()
    shippingBundleId = models.IntegerField()
    customerIdNum = models.IntegerField()
    customerName = models.TextField(max_length=255)
    shippingFee = models.IntegerField()
    invoiceNumber = models.TextField(null=True)
    deliveryStatusCode = models.TextField(null=True)
    postCode = models.IntegerField()
    orderRequirements = models.TextField()
    recipientAddressOne = models.TextField()
    recipientAddressTwo = models.TextField()
    customerCellNum2 = models.IntegerField(null=True)
    customerPhoneNum = models.IntegerField()
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
    modifiedAt = models.IntegerField()
    customerCellNum1 = models.IntegerField()
    customerCellNum = models.IntegerField()
    safeNumber = models.IntegerField()
    safeNumberSrl = models.TextField(max_length=255)

    def __str__(self):
        return self.recipientName