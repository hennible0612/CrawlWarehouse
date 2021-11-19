from django.urls import path

from . import views

app_name = 'mallboard'

urlpatterns = [
    path('',views.mallboard),
    path('coupang/', views.coupang, name='coupang'),
    path('esm/',views.esm),
    path('interpark/', views.interpark),

    path('coupang/<int:customer_id>/',views.customerdetail, name='customerdetail')
]