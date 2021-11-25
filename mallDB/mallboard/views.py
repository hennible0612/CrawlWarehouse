from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Coupang, Interpark #쿠팡 모델 가져옴
from django.core.paginator import Paginator
# from crawlwarehouse import crawlInterpark

# from function import addInterpark
# from CrawlWebsite import *

# Create your views here.

@login_required(login_url='common:login')
def mallboard(request):
    return render(request,'base.html')

@login_required(login_url='common:login')
def interpark(request):
    """
    interpark 주문 목록 출력
    """
    # 입력 파라미터

    if request.method == "post":
        print("post")
    page = request.GET.get('page', '1')

    customer_list = Interpark.objects.order_by('-id')

    paginator = Paginator(customer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # return HttpResponse("Coupang에 오신것을 환영합니다.")

    name = {'Customer_list': page_obj}

    return render(request, 'interpark/interpark_list.html',name)

@login_required(login_url='common:login')
# def interparkdatefilter(request,firstdate):
def interparkdatefilter(request):

    firstdate = request.GET.get('firstdate')
    firstdate = request.GET.get('seconddate')
    print('firstdate with GET: ',firstdate)
    # page = request.GET.get('page', '1')
    #
    #
    firstdate = request.POST['firstdate']
    seconddate = request.POST['seconddate']
    customer_list = Interpark.objects.filter(orderDate__range=[firstdate, seconddate])

    paginator = Paginator(customer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    name = {'Customer_list': page_obj, 'page': page}
    return render(request, 'interpark/interpark_list.html', name)
    #
    #
    # page = request.GET.get('page', '1')
    # firstdate = request.POST['firstdate']
    # seconddate = request.POST['seconddate']
    # customer_list = Interpark.objects.filter(orderDate__range=[firstdate, seconddate])
    #
    # paginator = Paginator(customer_list, 10)  # 페이지당 10개씩 보여주기
    # page_obj = paginator.get_page(page)
    # name = {'Customer_list': page_obj, 'page': page}
    # return render(request, 'interpark/interpark_list.html', name)





@login_required(login_url='common:login')
def interparkcustomerdetail(request, customer_id):
    """
    detail 출력
    """
    customer = get_object_or_404(Interpark, pk=customer_id)
    # customer = Coupang.objects.get(id=customer_id)
    context = {'customer': customer} # ' ' 사이에있는 이름으로 html에서 접근해야함
    return render(request,'interpark/interpark_customer_detail.html',context)

@login_required(login_url='common:login')
def coupang(request):
    """
    coupang 주문 목록 출력
    """

    customer_list = Coupang.objects.order_by('id')
    name = {'Customer_list': customer_list}
    # return HttpResponse("Coupang에 오신것을 환영합니다.")
    return render(request, 'coupang/coupang_list.html',name)

@login_required(login_url='common:login')
def customerdetail(request, customer_id):
    """
    detail 출력
    """
    customer = get_object_or_404(Coupang, pk=customer_id)
    # customer = Coupang.objects.get(id=customer_id)
    context = {'customer': customer} # ' ' 사이에있는 이름으로 html에서 접근해야함
    return render(request,'coupang/customer_detail.html',context)

@login_required(login_url='common:login')
def esm(request):
    return HttpResponse("Esm에 오신것을 환경합니다.")


import csv

@login_required(login_url='common:login')
def getneworder(request):
    # addInterpark()
    # crawlInterpark.crawlInterpark()
    with open('interpark.csv', encoding='UTF8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
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
            # p.save()

    return interpark(request)