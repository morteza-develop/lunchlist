from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


class UserInfo(models.Model):
    # user = models.m
    profileimage = models.ImageField(verbose_name= _('تصویر'))


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
        ("1", "صبحانه"),
        ("2", "نهار")
    )

    foodType = models.IntegerField(
        verbose_name=_("نوع غذا"), 
        choices=FOOD_CHOICES, 
        default=0
        )

    foodImage = models.ImageField(
        verbose_name=_("تصویر"),
        )
    
    class Meta:
        verbose_name = _("غذا")
        verbose_name_plural = _("غذاها")
    
    
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

    class Meta:
        verbose_name = _("منو")
        verbose_name_plural = _("منو ها")

