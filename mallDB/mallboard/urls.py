from django.urls import path

from . import views


from .views import base_views, coupang_views, interpark_views

app_name = 'mallboard'

urlpatterns = [

    #base_views.py


    path('',views.mallboard, name='mallboard'),
    # path('esm/',views.esm),
    path('coupang/', views.coupang, name='coupang'),
    path('coupang/<int:customer_id>/',views.customerdetail, name='customerdetail'),


    path('interpark/', views.interpark, name='interpark'),
    path('interpark/<int:customer_id>/', views.interparkcustomerdetail, name='interparkcustomerdetail'),

]