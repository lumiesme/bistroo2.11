from django.urls import path
from . import views

app_name = 'app_admin'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('food_list/', views.FoodListView.as_view(), name= 'food_list'),
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('food_update/<int:pk>', views.FoodUpdateView.as_view(), name='food_update'),
    path('food_delete/<int:pk>', views.FoodDeleteView.as_view(), name='food_delete'),
    path('menu_header/', views.MenuCategories.as_view(), name='menu_header'),
    path('food_create/', views.Foods.as_view(), name='food_create')
]