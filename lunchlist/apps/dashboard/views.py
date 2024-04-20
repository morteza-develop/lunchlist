from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    

def logoutView(request):
    logout(request)
    return redirect("login")

def dashboard_index(request):
    return render(request, "dashboard/lunchlist.html")