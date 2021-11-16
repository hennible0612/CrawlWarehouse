from django.contrib import admin
from .models import Esm,Coupang

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['productNum']


admin.site.register(Esm)
admin.site.register(Coupang)
