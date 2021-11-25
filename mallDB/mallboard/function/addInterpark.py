import csv

from mallboard.models import Interpark


with open('interpark.csv', encoding='UTF8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = Interpark(orderDate=row["orderDate"] ,recipientAddress=row["recipientAddress"]
                      ,serviceUsageFee=["serviceUsageFee"] ,callsafeYn=["callsafeYn"],
                      clmreqCnt=row["clmreqCnt"] ,crmCouponDiscountAmount=row["crmCouponDiscountAmount"]
                      ,currentOrdclmprdStat=row["currentOrdclmprdStat"],
                      currentOrdclmprdStatNm=row["currentOrdclmprdStatNm"] ,shippingFee=["shippingFee"]
                      ,orderAmount1=["orderAmount1"] ,orderType=["orderType"],
                      delvAttbt=row["delvAttbt"], delvAttbtNm=row["delvAttbtNm"]
                      ,orderRequirements=row["orderRequirements"] ,delvWhDt=["delvWhDt"] ,delvwhOrdNo=["delvwhOrdNo"],
                      delvwhPreDate=row["delvwhPreDate"] ,dtlAddr=row["dtlAddr"] ,dtlAddrDoro=row["dtlAddrDoro"]
                      ,couponAppliedAmount=["couponAppliedAmount"],
                      discountAmount=row["discountAmount"] ,expectedSellingFee=row["expectedSellingFee"]
                      ,expectedSettlementAmt=row["expectedSettlementAmt"],
                      sellerCode=row["sellerCode"] ,externalPrdNo=row["externalPrdNo"] ,feeRate=row["feeRate"]
                      ,hdelvMafcEntrNoDefault=row["hdelvMafcEntrNoDefault"],
                      inpkCouponDiscountAmount=row["inpkCouponDiscountAmount"] ,interestFreeFee=row["interestFreeFee"]
                      ,ipointDcAmt=row["ipointDcAmt"] ,ipointFee=row["ipointFee"],
                      manufacture=row["manufacture"] ,marginRate=row["marginRate"]
                      ,modDelvwhPreDate=row["modDelvwhPreDate"] ,modDelvwhPreDateYn=row["modDelvwhPreDateYn"],
                      odpDtlAddr=row["odpDtlAddr"], odpDtlAddrDoro=row["odpDtlAddrDoro"] ,odpZipAddr=row["odpZipAddr"]
                      ,odpZipAddrDoro=row["odpZipAddrDoro"],
                      odpZipNo=row["odpZipNo"] ,odpZipNoDoro=row["odpZipNoDoro"] ,optFnm=row["optFnm"]
                      ,optParentSeq=row["optParentSeq"] ,optPrdTp=row["optPrdTp"],
                      optPrdTpNm=row["optPrdTpNm"] ,orderAmount=row["orderAmount"] ,ordEngnm=row["ordEngnm"]
                      ,customerId=["customerId"] ,customerCellNum=row["customerCellNum"],
                      customerName=row["customerName"] ,ordSeq=row["ordSeq"] ,customerCellNum2=row["customerCellNum2"]
                      ,ordclmDts=row["ordclmDts"] ,ordclmNo=row["ordclmNo"],
                      paidDate=row["paidDate"], parentClaimRequestYn=row["parentClaimRequestYn"]
                      ,productNum=row["productNum"] ,paymentMethod=row["paymentMethod"],
                      productName=row["productName"] ,productNum1=row["productNum1"]
                      ,preUseUnitcost=row["preUseUnitcost"] ,unitPrice=row["unitPrice"] ,unitSold=row["unitSold"],
                      customerPhoneNum=row["customerPhoneNum"] ,recipientName=row["recipientName"], recipientCellNum=row["recipientCellNum"] ,recipientIdNum=row["recipientIdNum"],
                      residentNo=row["residentNo"] ,rowNum=row["rowNum"] ,unitSoldTotal=row["unitSoldTotal"]
                      ,specialYn=row["specialYn"] ,todayDelvYn=row["todayDelvYn"],
                      totalFee=row["totalFee"] ,totalPrice=row["totalPrice"] ,totalRecCnt=row["totalRecCnt"], zipAddr=row["zipAddr"] ,zipAddrDoro=row["zipAddrDoro"] ,postCode=row["postCode"],
                      zipNo=row["zipNo"] ,zipNoDoro=row["zipNoDoro"]


                      )
        p.save()