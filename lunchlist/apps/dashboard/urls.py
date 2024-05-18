from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_index , name='dashboard'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('menulist/', views.menulist_view , name='menulist'),
    path('foodlist/', views.foodlist_view , name='foodlist'),
    path('reserveform/', views.reserve_form_view , name='reserveform'),
    path('createMenu/', views.create_menu_view , name='createMenu'),
    path('createFood/', views.create_food_view , name='createFood'),
    path('updateFood/<int:pk>', views.update_food_view , name='updateFood'),
    path('add_item_menu/<int:pk>/', views.add_item_menu, name='add_item_menu'),

]
