from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_index , name='index'),
    path('login/', views.login_view , name='login')
]
