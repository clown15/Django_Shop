from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name="product.html"
    # html에서 사용할 변수 명
    context_object_name="product_list"

class ProductCreate(FormView):
    template_name = "register_product.html"
    form_class=RegisterForm
    success_url = "/product/"

class ProduectDetail(DetailView):
    template_name = "product_detail.html"
    queryset = Product.objects.all()
    context_object_name = "product"