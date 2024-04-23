from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_index , name='dashboard'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
]
