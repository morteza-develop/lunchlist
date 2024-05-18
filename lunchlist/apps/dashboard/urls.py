from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_index , name='dashboard'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('menulist/', views.menulist_view , name='menulist'),
    path('foodlist/', views.foodlist_view , name='foodlist'),
    path('reserveform/<int:pk>', views.reserve_form_view , name='reserveform'),
    path('createMenu/', views.create_menu_view , name='createMenu'),
    path('updateMenu/<int:pk>', views.update_menu_view , name='updateMenu'),
    path('deactivateMenu/<int:pk>', views.deactivate_menu_view , name='deactivateMenu'),
    path('createFood/', views.create_food_view , name='createFood'),
    path('updateFood/<int:pk>', views.update_food_view , name='updateFood'),
    path('deleteFood/<int:pk>', views.delete_food_view , name='deleteFood'),
    path('add_item_menu/<int:pk>/', views.add_item_menu, name='add_item_menu'),

]
