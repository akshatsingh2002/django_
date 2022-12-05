from django.contrib import admin

from .models import *
# Register your models here.
# admin.site.register(query)
@admin.register(query)
class kuchbhi(admin.ModelAdmin):
    list_display = ["id","email","Msg"]
@admin.register(material)
class products(admin.ModelAdmin):
    list_display = ["name","price","desc","img"]