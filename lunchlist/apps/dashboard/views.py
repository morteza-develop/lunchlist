from django.shortcuts import render

def dashboard_index(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, 'dashboard/login.html')