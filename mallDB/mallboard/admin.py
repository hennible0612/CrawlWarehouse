from django.contrib import admin

# Register your models here.
from mallboard.models import Coupang



class SearchCustomer(admin.ModelAdmin):
    search_fields = ['customerName']

admin.site.register(Coupang,SearchCustomer)
