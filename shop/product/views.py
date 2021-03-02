from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
# Create your views here.

class Product_List(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'product_list'

class Product_Detail(DetailView):
    template_name = 'detail.html'
    context_object_name = 'product'
    queryset = Product.objects.all()