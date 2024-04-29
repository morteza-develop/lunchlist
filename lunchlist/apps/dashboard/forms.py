from django import forms
from .models import Food , Menu

class FoodForm(forms.ModelForm):
    foodName = forms.CharField(
        max_length=100,
        label="نام غذا",
        required=True,
        widget=forms.TextInput(attrs={'class':'form-input'})
    )

    description = forms.CharField(
        max_length=250,
        label="توضیحات",
        required=True,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-input'})
    )

    price = forms.DecimalField(
        label="قیمت غذا",
        required=True,
        decimal_places=2,
        min_value=0.01,
        widget=forms.TextInput(attrs={'class':'form-input'})
    )

    FOOD_CHOICES = (
        (1, "صبحانه"),
        (2, "ناهار"),
    )

    foodType = forms.ChoiceField(
        label="نوع غذا",
        choices=FOOD_CHOICES,
        widget=forms.RadioSelect(),
        required=True,
    )

    foodImage = forms.ImageField(
        label="تصویر",
        required=False,
        help_text="تصویری از غذای خود را آپلود کنید."
    )

    class Meta:
        model = Food
        fields = ['foodName', 'description', 'price', 'foodType', 'foodImage']


class MenuForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        label="نام منو",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام منو را وارد کنید'})
    )

    expire = forms.DateField(
        label="تاریخ انقضاء",
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'تاریخ انقضاء را انتخاب کنید'})
    )

    status = forms.ChoiceField(
        label="وضعیت منو",
        choices=Menu.MENU_STATUS,
        widget=forms.RadioSelect(),
        required=True,
        help_text="وضعیت این منو را انتخاب کنید."
    )

    class Meta:
        model = Menu
        fields = ['name', 'expire', 'status']