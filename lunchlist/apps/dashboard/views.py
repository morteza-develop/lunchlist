from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from . import models
from datetime import datetime
from apps.dashboard.forms import FoodForm, MenuForm
from apps.dashboard.models import Menu , Food , MenuItem
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import moment
import jdatetime

from datetime import date




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(
                request, ('خطای ورود ...! نام کاربری یا رمز عبور صحیح نیست !!!'))
            return redirect("login")
    else:
        return render(request, "dashboard/login.html", {})
    

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def dashboard_index(request):
    return render(request, "dashboard/dashboard.html")


@login_required(login_url="login")
def menulist_view(request):

    all_menu = Menu.objects.all().order_by('-id').values()

    context ={
        "all_menu":all_menu
    }

    return render(request, "dashboard/menulist.html",context)


@login_required(login_url="login")
def foodlist_view(request):

    all_food = Food.objects.all()

    context = {
        "all_food": all_food
    }
    return render(request, "dashboard/foodlist.html", context)


@login_required(login_url="login")
def reserve_form_view(request):

    return render(request, "dashboard/reserve-form.html")


@login_required(login_url="login")
def create_menu_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        expire = request.POST['expire']
        status = int(request.POST['status'])
        createDate = datetime.now()

        new_menu = Menu(
            name=name,
            expire=expire,
            status=status,
            createDate=createDate
        )

        new_menu.save()

        message = "منوی جدید با موفقیت ایجاد شد!"
        return redirect("menulist")

    else:
        return render(request, "dashboard/create-menu.html")
    # return render(request, "dashboard/create-menu.html")




@login_required(login_url='login')
def add_item_menu(request, pk):
    try:
        get_menu = Menu.objects.get(pk=pk)
        print(get_menu)
    except Menu.DoesNotExist:
        return HttpResponse('Menu does not exist', status=404)

    if request.method == 'POST':
        food_id = int(request.POST.get('food', '0')) 
        date_of_serving = request.POST.get('date_of_serving', '').strip()

        if not date_of_serving:
            return HttpResponse("Date of serving is required.", status=400)

        try:

            j_date = jdatetime.datetime.strptime(date_of_serving, '%Y/%m/%d').date()
            g_date = j_date.togregorian()
            gregorian_date_str = g_date.strftime('%Y-%m-%d')
        except ValueError as e:
            print("Date conversion error:", e)
            return HttpResponse('Invalid date format', status=400)

        try:
            selected_food = Food.objects.get(pk=food_id)
        except Food.DoesNotExist:
            return HttpResponse('Food item does not exist', status=404)

        new_item_menu = MenuItem(
            menu=get_menu,
            food=selected_food,
            date_of_serving=gregorian_date_str
        )
        new_item_menu.save()

    get_all_food = Food.objects.all()
    get_menu_items = MenuItem.objects.filter(menu= pk)
    print(get_menu_items)
    context = {
        "get_menu": get_menu,
        "get_all_food": get_all_food,
        "set_menu_id": pk,
        "get_menu_items":get_menu_items
    }
    return render(request, "dashboard/add-item-menu.html", context)




@login_required(login_url="login")
def create_food_view(request):
    if request.method == 'POST':
        food_name = request.POST['foodName']
        description = request.POST['description']
        price = request.POST['price']
        food_type = request.POST['foodType']
        food_image = request.FILES.get('foodImage')  # Access uploaded image

        # Validate data (improvements based on feedback)
        if not food_name:
            messages.error(request, 'Please enter a name for the food.')
            return render(request, 'add_food.html', {'food_types': Food.FOOD_CHOICES})  # Pass food types for form
        try:
            price = int(price)  # Attempt to convert price to integer
        except ValueError:
            messages.error(request, 'Please enter a valid price (numbers only).')
            return render(request, 'add_food.html', {'food_types': Food.FOOD_CHOICES})

        # Create and save Food object
        new_food = Food.objects.create(
            foodName=food_name,
            description=description,
            price=price,
            foodType=food_type,
            foodImage=food_image  # Save uploaded image
        )

        messages.success(request, 'Food added successfully!')
        return redirect('createFood') 
    return render(request, "dashboard/create-food.html")

