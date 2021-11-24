from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Coupang, Interpark #쿠팡 모델 가져옴
from django.core.paginator import Paginator



# Create your views here.

def mallboard(request):
    return render(request,'base.html')

def interpark(request):
    """
    interpark 주문 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')



    customer_list = Interpark.objects.order_by('id')


    paginator = Paginator(customer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # return HttpResponse("Coupang에 오신것을 환영합니다.")

    name = {'Customer_list': page_obj}

    return render(request, 'interpark/interpark_list.html',name)

def interparkcustomerdetail(request, customer_id):
    """
    detail 출력
    """
    customer = get_object_or_404(Interpark, pk=customer_id)
    # customer = Coupang.objects.get(id=customer_id)
    context = {'customer': customer} # ' ' 사이에있는 이름으로 html에서 접근해야함
    return render(request,'interpark/interpark_customer_detail.html',context)


def coupang(request):
    """
    coupang 주문 목록 출력
    """

    customer_list = Coupang.objects.order_by('id')
    name = {'Customer_list': customer_list}
    # return HttpResponse("Coupang에 오신것을 환영합니다.")
    return render(request, 'coupang/coupang_list.html',name)

def customerdetail(request, customer_id):
    """
    detail 출력
    """
    customer = get_object_or_404(Coupang, pk=customer_id)
    # customer = Coupang.objects.get(id=customer_id)
    context = {'customer': customer} # ' ' 사이에있는 이름으로 html에서 접근해야함
    return render(request,'coupang/customer_detail.html',context)

def esm(request):
    return HttpResponse("Esm에 오신것을 환경합니다.")