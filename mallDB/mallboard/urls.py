from django.urls import path

from . import views

app_name = 'mallboard'

urlpatterns = [
    path('',views.mallboard, name='mallboard'),
    path('mallboard/esm/',views.esm, name='esm'),

    # 쿠팡 url
    path('coupang/', views.coupang, name='coupang'),
    path('coupang/<int:customer_id>/',views.coupangcustomerdetail, name='coupangcustomerdetail'),

    #인터파크 url
    path('interpark/', views.interpark, name='interpark'),
    path('interpark/<int:customer_id>/', views.interparkcustomerdetail, name='interparkcustomerdetail'),
    path('mallboard/interparkdatefilter', views.interparkdatefilter, name='interparkdatefilter'),

    #ESM url
    path('esm/', views.esm, name='esm'),
    path('esm/<int:customer_id>/', views.esmcustomerdetail, name='esmcustomerdetail'),


    #<str: ... > <int:...>
    # path('mallboard/getneworder/',views.getneworder, name="getneworder")
    path('mallboard/getneworder/<str:mall_name>',views.getneworder, name="getneworder")
]