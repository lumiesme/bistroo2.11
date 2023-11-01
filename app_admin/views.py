import urllib.parse
from urllib.request import urlopen
import json
from django.urls import reverse_lazy
from .models import Category

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from django.conf import settings
from django.core.paginator import Paginator
from .models import *


class HomeView(TemplateView):
    template_name = 'app_admin/index.html'

class FoodListView(ListView):
    # model_list.html -> student_list.html
    template_name = 'app_admin/food_list.html'
    model = Category # Connected to Models Student-siit tuleb info
    queryset = Category.objects.order_by('name')  # nime jargi sorteeritud, result ordered by name
    context_object_name = 'categories'  # object_list is default
    paginate_by = 10  # 10 per page in ListView

class CategoryCreateView(CreateView):
    template_name = 'app_admin/category_create.html'
    fields = "__all__"
    #form_class = CategoryCreateForm
    model = Category
    success_url = reverse_lazy('app_admin:food_list')

class FoodUpdateView(UpdateView):
    template_name = 'app_admin/food_update.html'
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('app_admin:food_list')

class FoodDeleteView(DeleteView):
    template_name = 'app_admin/food_delete.html'
    model = Category
    success_url = reverse_lazy('app_admin:food_list')

class MenuCategories(CreateView):
    template_name = 'app_admin/menu_header.html'
    success_url = reverse_lazy('app_admin:food_list')
    queryset = MenuCategory.objects.order_by('teema_paev')
    fields = "__all__"

class Foods(CreateView):
    template_name = 'app_admin/food_create.html'
    #kuupaev = datetime('%d.%m.%Y')
    toidu_nimetus = models.CharField(max_length=1000,null=True, blank=True, unique=True, verbose_name="Sisesta toidu nimetus")
    taishind = models.IntegerField(null=False, blank=True)  # hetkel ainult taishind, peaks olema kakomaga arv
    poolhind = models.IntegerField(null=False, blank=True)
    #on_menuus =
    queryset = Foods_listing.objects.order_by('toidu_nimetus')
    fields = '__all__'
