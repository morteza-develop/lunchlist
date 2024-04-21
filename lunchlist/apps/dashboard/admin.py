from django.contrib import admin
from apps.dashboard.models import *


class FoodAdmin(admin.ModelAdmin):
    list_display= ("foodName","foodType","price")

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name","createDate","expire")

admin.site.register(Food, FoodAdmin)
admin.site.register(Menu, MenuAdmin)