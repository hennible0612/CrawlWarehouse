from django.urls import path

from . import views

app_name = 'mallboard'

urlpatterns = [
    path('',views.mallboard),
    path('esm/',views.esm),
    path('coupang/', views.coupang, name='coupang'),
    path('coupang/<int:customer_id>/',views.customerdetail, name='customerdetail'),


    path('interpark/', views.interpark, name='interpark'),
    path('interpark/<int:customer_id>/', views.interparkcustomerdetail, name='interparkcustomerdetail'),

]