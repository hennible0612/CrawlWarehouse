from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Coupang, Interpark #쿠팡 모델 가져옴
from django.core.paginator import Paginator
import sys
from .myfunction import addInterpark
import os
os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
from CrawlWebsite.crawlwarehouse import crawlInterpark



@login_required(login_url='common:login')
def mallboard(request):
    return render(request,'base.html')

@login_required(login_url='common:login')
def interpark(request):
    """
    interpark 주문 목록 출력
    """
    # 입력 파라미터

    page = request.GET.get('page', '1') #?으로 뒤에 딸려온거 get ?이 없을경우 default 로 1

    customer_list = Interpark.objects.order_by('-id')

    paginator = Paginator(customer_list, 10)  #customer_list를 가져와 10개로 나누고 paginator에 넣음
    page_obj = paginator.get_page(page) #paginator를 사용하여 요청된 객체들에 대한 페이징 객체를 만들고, 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경된다. {{객체.속성}}

    # https://wikidocs.net/71240

    context = {'Customer_list': page_obj, 'target_url': 'interpark'} #Customer_list로 page_obj를 보냄 즉, 템플릿에서는 {{Customer_list.id}}로 객체 접근

    return render(request, 'interpark/interpark_list.html',context) #그리고

@login_required(login_url='common:login')
def interparkdatefilter(request):
# def interparkdatefilter(request):

    firstdate = request.GET.get('firstdate')
    seconddate = request.GET.get('seconddate')
    page = request.GET.get('page', '1')

    customer_list = Interpark.objects.filter(orderDate__range=[firstdate, seconddate])

    paginator = Paginator(customer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'Customer_list': page_obj, 'page': page, 'firstdate':firstdate, 'seconddate':seconddate}
    return render(request, 'interpark/interpark_list.html', context,)
    # return HttpResponse("firstDate" + firstdate + "secondDate" + seconddate)
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
def interparkcustomerdetail(request, customer_id): #href로 이 view 부를때 인자도 같이 받는다.   ******** 나중에 이걸로 내가 어느몰에 있는지 확인해야할듯
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
def getneworder(request, mall_name):

    if (mall_name =="coupang"):
        print("couapng")
        return HttpResponse("coupang")
    elif (mall_name=="interpark"):
        print("interpark")
        crawlInterpark.crawlInterpark()
        addInterpark.addInterpark()

        return interpark(request)
    else:
        print("err 원하는거 못잡음")
        return HttpResponse("원하는거 못잡음")

    #
    # print(request)
    # #
    #
    #