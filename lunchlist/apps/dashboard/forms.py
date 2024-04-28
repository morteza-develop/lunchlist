from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    foodName = forms.CharField(
        max_length=100,
        label="نام غذا",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام غذا را وارد کنید'})
    )

    description = forms.CharField(
        max_length=250,
        label="توضیحات",
        required=True,
        widget=forms.Textarea(attrs={'rows': 3})
    )

    price = forms.DecimalField(
        label="قیمت غذا",
        required=True,
        decimal_places=2,
        min_value=0.01
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
        help_text="نوع غذای این غذا را انتخاب کنید."
    )

    foodImage = forms.ImageField(
        label="تصویر",
        required=False,
        help_text="تصویری از غذای خود را آپلود کنید."
    )

    class Meta:
        model = Food
        fields = ['foodName', 'description', 'price', 'foodType', 'foodImage']