
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Coupang


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