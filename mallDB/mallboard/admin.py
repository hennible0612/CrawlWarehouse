from django.contrib import admin


from django.contrib import admin

# Register your models here.
from mallboard.models import Coupang,Interpark,Esm



class SearchCustomer(admin.ModelAdmin):
    search_fields = ['customerName']

admin.site.register(Coupang,SearchCustomer)
admin.site.register(Interpark,SearchCustomer)
admin.site.register(Esm,SearchCustomer)
