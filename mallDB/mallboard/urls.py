from django.urls import path

from . import views

app_name = 'mallboard'

urlpatterns = [
    path('',views.mallboard, name='mallboard'),
    path('mallboard/esm/',views.esm, name='esm'),


    path('coupang/', views.coupang, name='coupang'),
    path('coupang/<int:customer_id>/',views.customerdetail, name='customerdetail'),


    path('interpark/', views.interpark, name='interpark'),
    path('interpark/<int:customer_id>/', views.interparkcustomerdetail, name='interparkcustomerdetail'),

    path('mallboard/interparkdatefilter', views.interparkdatefilter, name='interparkdatefilter'),

    #<str: ... > <int:...>
    # path('mallboard/getneworder/',views.getneworder, name="getneworder")
    path('mallboard/getneworder/<str:mall_name>',views.getneworder, name="getneworder")
]