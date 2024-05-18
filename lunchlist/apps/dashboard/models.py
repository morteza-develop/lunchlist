from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import os



class UserInfo(models.Model):
    # user = models.m
    profileimage = models.ImageField(
        upload_to="static/images/",
        verbose_name= _('تصویر')
        )

# FOOD Model \\\\\\\\\\\\\\\\\\\\\
class Food(models.Model):
    foodName = models.CharField(
        max_length=100,
        verbose_name=_("نام غذا")
        )
    description = models.CharField(
        max_length=250, 
        verbose_name=_("توضیحات")
        )
    price = models.IntegerField(
        null=True, 
        verbose_name=_("قیمت غذا"))
    
    FOOD_CHOICES  = (
        ( 1 , "صبحانه"),
        ( 2 , "نهار")
    )

    foodType = models.IntegerField(
        verbose_name=_("نوع غذا"), 
        choices=FOOD_CHOICES, 
        default=0
        )

    foodImage = models.ImageField(
        upload_to="static/images/", 
        blank=True, 
        verbose_name=_("تصویر"),
        )

    def save(self, *args, **kwargs):
        if self.foodImage:
            # Extract only the filename
            self.foodImage.name = os.path.basename(self.foodImage.name)
        super(Food, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.foodName 
    
    class Meta:
        verbose_name = _("غذا")
        verbose_name_plural = _("غذاها")
    
# MENU Model \\\\\\\\\\\\\\\\\\\\\\\
class Menu(models.Model):
    name = models.CharField(
        verbose_name=_("نام منو"),
        max_length=100,
    )
    createDate = models.DateField(
        verbose_name=_("زمان ایجاد"),
        auto_now_add=True,
    )
    expire = models.DateField(
        verbose_name=_("زمان انقضاء"),
    )

    MENU_STATUS  = (
        ( 0, "بسته"),
        ( 1, "باز"),
    )

    status = models.IntegerField(
        verbose_name=_("وضعیت منو"),        
        choices=MENU_STATUS, 
        default=0
    )

    def __str__(self): 
        return self.name

    class Meta:
        verbose_name = _("منو")
        verbose_name_plural = _("منو ها")


# MENU item Model \\\\\\\\\\\\\\\\\\\\\\\
class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,   
        on_delete=models.CASCADE,
        verbose_name=_("انتخاب منو")
        )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name=_("انتخاب غذا")
    )

    date_of_serving = models.DateField(
        verbose_name=_("تاریخ سرور غذا"),
    )

    def __str__(self):
        return str(self.menu)
    

    class Meta:
        verbose_name = _("آیتمهای منو")
        verbose_name_plural = _("آیتمهای منو")


# RESERVE Model \\\\\\\\\\\\\\\\\\\\\\\
class Reservation(models.Model):
    userName = models.ManyToManyField(
        'auth.User', 
        verbose_name=_("کاربر")
        )
    menuItem = models.ForeignKey(
        MenuItem, 
        on_delete=models.CASCADE,
        verbose_name="منو",
        default=1,
        )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name=_("غذا")
    )

    class Meta:
        verbose_name = _("رزرو")
        verbose_name_plural = _("رزروهای انجام شده")

