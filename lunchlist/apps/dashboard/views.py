from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from . import models
from apps.dashboard.models import Menu , Food
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




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

    all_menu = Menu.objects.all().order_by('-createDate').values()

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