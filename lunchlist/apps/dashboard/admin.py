from django.contrib import admin
from apps.dashboard.models import *


class FoodAdmin(admin.ModelAdmin):
    list_display= ("foodName","foodType","price")

class MenuAdmin(admin.ModelAdmin):
    list_display = ("name","createDate","expire")

class ReservationAdmin(admin.ModelAdmin):
    # list_display = ("User")
    pass

class MenuItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Food, FoodAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(MenuItem, MenuItemAdmin)