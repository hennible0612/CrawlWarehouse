from django.urls import path

from . import views

urlpatterns = [
    path('',views.mallboard),
    path('coupang/', views.coupang),
    path('esm/',views.esm),


    path('coupang/<int:customer_id>/',views.customerdetail)
]