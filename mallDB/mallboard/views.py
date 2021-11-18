from django.shortcuts import render
from django.http import HttpResponse
from .models import Coupang #쿠팡 모델 가져옴




# Create your views here.

def mallboard(request):
    return HttpResponse("mallboard에 오신것을 환영합니다.")

def coupang(request):
    """
    coupang 주문 목록 출력
    """
    customer_list = Coupang.objects.order_by('id')
    name = {'Customer_list': customer_list}
    # return HttpResponse("Coupang에 오신것을 환영합니다.")
    return render(request, 'coupang/coupang_list.html',name)

def esm(request):
    return HttpResponse("Esm에 오신것을 환경합니다.")